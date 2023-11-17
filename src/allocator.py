from intermediate_rep import DoublyLinkedList
from intermediate_rep import Node 
import constants
import sys 

class Allocator: 

    def __init__(self, num_regs, renamed_ir: DoublyLinkedList, vr_name, max_live): 
        self.num_regs = num_regs 
        self.renamed_ir = renamed_ir 
        self.vr_name = vr_name 
        self.max_live = max_live 
        self.spill_loc = 32768

        self.reserved_reg = num_regs - 1
        self.registers= []
        self.marked = None 
        if max_live <= num_regs: 
            self.registers.append(self.reserved_reg)
        for reg in range(num_regs - 2, -1, -1): 
            self.registers.append(reg)

        self.vr_pr = [None] * vr_name
        self.pr_vr = [None] * num_regs
        self.vr_spill = [None] * vr_name
        self.vr_constant = [None] * vr_name
        self.pr_nu = [float('inf')] * num_regs 

    def get_pr(self, vr, nu, current): 
        pr = None 
        if len(self.registers) != 0: 
            pr = self.registers.pop()
        else: 
            pr = self.spill(current)
        
        self.vr_pr[vr] = pr 
        self.pr_vr[pr] = vr 
        self.pr_nu[pr] = nu 

        return pr 
    
    def spill(self, current: Node): 
        curr_spill = 0
        spill_reg = 0
        spill_vr = 0 
        highest_nu = 0
        for idx in range(self.num_regs - 1): 
            if self.marked == idx: 
                continue 
            if self.pr_nu[idx] > highest_nu: 
                spill_reg = idx 
                highest_nu = self.pr_nu[idx]
                spill_vr = self.pr_vr[idx]
        
        if self.vr_spill[spill_vr] == None: 
            curr_spill = self.spill_loc
            self.vr_spill[spill_vr] = self.spill_loc
            self.spill_loc += 4
        else: 
            curr_spill = self.vr_spill[spill_vr]

        self.vr_pr[spill_vr] = None

        new_node = Node(sys.maxsize, constants.LOADI, curr_spill, None, None, constants.LOADI)
        new_node.operand3[2] = self.reserved_reg 
        self.insert_left(current, new_node)

        new_node2 = Node(sys.maxsize, constants.MEMOP, None, None, None, constants.STORE)
        new_node2.operand1[2] = spill_reg
        new_node2.operand3[2] = self.reserved_reg
        self.insert_left(current, new_node2)

        return spill_reg  

    def free_pr(self, pr): 
        self.vr_pr[self.pr_vr[pr]] = None
        self.pr_vr[pr] = None
        self.pr_nu[pr] = float('inf')

        self.registers.append(pr)

    def restore(self, vr, pr, current): 
        if self.vr_constant[vr] != None: 
            new_node = Node(sys.maxsize, constants.LOADI, self.vr_constant[vr], None, None, constants.LOADI)
            new_node.operand3[2] = pr
            self.insert_left(current, new_node)
        
        else: 
            new_node = Node(sys.maxsize, constants.LOADI, self.vr_spill[vr], None, None, constants.LOADI)
            new_node.operand3[2] = self.reserved_reg
            self.insert_left(current, new_node)

            new_node2 = Node(sys.maxsize, constants.MEMOP, None, None, None, constants.LOAD)
            new_node2.operand1[2] = self.reserved_reg
            new_node2.operand3[2] = pr 
            self.insert_left(current, new_node2)

    
    def insert_left(self, current: Node, new_node: Node): 
        if current == self.renamed_ir.head: 
            new_node.next = current 
            new_node.prev = None 
            current.prev = new_node 
            self.renamed_ir.head = new_node 
        else: 
            new_node.next = current 
            new_node.prev = current.prev 
            current.prev.next = new_node 
            current.prev = new_node

    def remove(self, current: Node): 
        if current == self.renamed_ir.head: 
            self.renamed_ir.head = current.next 
            current.next.prev = None 
        elif current == self.renamed_ir.tail: 
            self.renamed_ir.tail = current.prev 
            current.prev.next = None 
        else: 
            current.prev.next = current.next 
            current.next.prev = current.prev 

    def allocate(self): 
        current = self.renamed_ir.head 

        while current: 
            self.marked = None 

            if current.opcode == constants.OUTPUT or current.opcode == constants.NOP: 
                current = current.next 
                continue 
            elif current.opcode == constants.LOADI: 
                self.vr_constant[current.operand3[1]] = current.operand1[0]
                self.remove(current) 

            elif current.spec_op == constants.STORE: 
                # For use 
                op1 = current.operand1  # OP 1 
                # Allocates use 
                pr1 = self.vr_pr[op1[1]] # Allocates use 
                if pr1 == None:
                    pr1 = self.get_pr(op1[1], op1[3], current)
                    op1[2] = pr1
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked = pr1


                op3 = current.operand3  # OP 3 
                # Allocates use 
                pr3 = self.vr_pr[op3[1]] 
                if pr3 == None: 
                    pr3 = self.get_pr(op3[1], op3[3], current)
                    op3[2] = pr3
                    self.restore(op3[1], op3[2], current)
                else: 
                    op3[2] = pr3 
                self.marked = pr3
                # Last use 
                if op1[3] == float('inf') and op1[2] != None and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])
                if op3[3] == float('inf') and op3[2] != None and self.pr_vr[op3[2]] != None: 
                    self.free_pr(op3[2])

                self.marked = None 
            elif current.spec_op == constants.LOAD: 
                # For use 
                op1 = current.operand1  # OP 1 
                # Allocates use 
                pr1 = self.vr_pr[op1[1]]
                if pr1 == None: 
                    pr1 = self.get_pr(op1[1], op1[3], current)
                    op1[2] = pr1
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked = pr1
                # Last use 
                if op1[3] == float('inf') and op1[2] != None and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])

                self.marked = None 
                # For definition
                op3 = current.operand3  # OP 3
                pr3 = self.get_pr(op3[1], op3[3], current)
                op3[2] = pr3
                self.marked = pr3
            else: 
                # For use 
                op1 = current.operand1  # OP 1
                # Allocates use  
                pr1 = self.vr_pr[op1[1]]
                if pr1 == None: 
                    pr1 = self.get_pr(op1[1], op1[3], current)
                    op1[2] = pr1
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked = pr1

                # For use 
                op2 = current.operand2  # OP 2 
                # Allocates use 
                pr2 = self.vr_pr[op2[1]]
                if pr2 == None: 
                    pr2 = self.get_pr(op2[1], op2[3], current)
                    op2[2] = pr2
                    self.restore(op2[1], op2[2], current)
                else: 
                    op2[2] = pr2
                self.marked = pr2
                # Last use 
                if op1[3] == float('inf') and op1[2] != None and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])
                if op2[3] == float('inf') and op2[2] != None and self.pr_vr[op2[2]] != None: 
                    self.free_pr(op2[2])

                self.marked = None 

                # For definition
                op3 = current.operand3  # OP 3
                pr3 = self.get_pr(op3[1], op3[3], current)
                op3[2] = pr3
                self.marked = pr3
            current = current.next

    def format(self): 
        current = self.renamed_ir.head
        while current: 
            if current.spec_op == constants.STORE: 
                print(f"store r{current.operand1[2]} => r{current.operand3[2]}")
            elif current.spec_op == constants.LOAD: 
                print(f"load r{current.operand1[2]} => r{current.operand3[2]}")         
            elif current.opcode == constants.LOADI: 
                print(f"loadI {current.operand1[0]} => r{current.operand3[2]}")
            elif current.spec_op == constants.ADD: 
                print(f"add r{current.operand1[2]}, r{current.operand2[2]} => r{current.operand3[2]}")
            elif current.spec_op == constants.SUB: 
                print(f"sub r{current.operand1[2]}, r{current.operand2[2]} => r{current.operand3[2]}")
            elif current.spec_op == constants.MULT: 
                print(f"mult r{current.operand1[2]}, r{current.operand2[2]} => r{current.operand3[2]}")
            elif current.spec_op == constants.LSHIFT: 
                print(f"lshift r{current.operand1[2]}, r{current.operand2[2]} => r{current.operand3[2]}")
            elif current.spec_op == constants.RSHIFT: 
                print(f"rshift r{current.operand1[2]}, r{current.operand2[2]} => r{current.operand3[2]}")
            elif current.opcode == constants.OUTPUT: 
                print(f"output {current.operand1[0]}")
            else: 
                print(f"nop")
            current = current.next 
