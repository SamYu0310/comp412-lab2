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
        self.registers = list(range(num_regs - 2, -1, -1))
        self.marked = list([0] * (num_regs - 2))
        if max_live <= num_regs: 
            self.registers.append(self.reserved_reg)
            self.marked.append(0)

        self.vr_pr = [None] * vr_name
        self.pr_vr = [None] * num_regs
        self.vr_spill = [None] * vr_name
        self.pr_nu = [float('inf')] * num_regs 

    def get_pr(self, vr, nu, current): 
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
        for idx in range(self.marked): 
            if self.marked[idx] == 1: 
                continue 
            if self.pr_nu[idx] > highest_nu: 
                spill_reg = idx 
                highest_nu = self.pr_nu[idx]
                spill_vr = self.pr_nu[idx]
        
        if self.vr_spill[spill_vr] == None: 
            curr_spill = self.spill_loc
            self.vr_spill[spill_vr] = self.spill_loc
            self.spill_loc += 4
        else: 
            curr_spill = self.vr_spill[spill_vr]

        self.vr_pr[spill_vr] = None

        new_node = Node(sys.maxint, constants.LOADI, curr_spill, None, None, constants.LOADI)
        new_node.operand3[2] = self.reserved_reg 
        self.insert_left(current, new_node)

        new_node2 = Node(sys.maxint, constants.MEMOP, None, None, None, constants.STORE)
        new_node2.operand1[2] = spill_reg
        new_node2.operand3[2] = self.reserved_reg
        self.insert_left(current, new_node2)

        return spill_reg  
    
    def free_pr(self, pr): 
        self.vr_pr[self.pr_vr[pr]] = None
        self.pr_vr[pr] = None
        self.pr_nu = float('inf')

        self.registers.append(pr)

    def restore(self, vr, pr, current): 
        new_node = Node(sys.maxint, constants.LOADI, self.vr_spill[vr], None, None, constants.LOADI)
        new_node.operand3[2] = self.reserved_reg
        self.insert_left(current, new_node)

        new_node2 = Node(sys.maxint, constants.MEMOP, None, None, None, constants.LOAD)
        new_node2.operand1 = self.reserved_reg
        new_node2.operand3 = pr 
        self.insert_left(current, new_node2)
    
    def insert_left(current: Node, new_node: Node): 
        new_node.next = current 
        new_node.prev = current.prev 
        current.prev.next = new_node 
        current.prev = new_node 

    def allocate(self): 
        current = self.renamed_ir.head 

        while current: 
            # Reset marks
            self.marked = list([0] * (self.num_regs - 2))
            if self.max_live <= self.num_regs: 
                self.marked.append(0)

            if current.opcode == constants.OUTPUT or current.opcode == constants.NOP: 
                current = current.next 
                continue 
            elif current.spec_op == constants.STORE: 
                # For use 
                op1 = current.operand1  # OP 1 
                # Allocates use 
                pr1 = self.vr_pr[op1[1]] # Allocates use 
                if pr1 == None:
                    op1[2] = self.get_pr(op1[1], op1[3], current)
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked[pr1] = 1
                # Last use 
                if op1[3] == float('inf') and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])

                op3 = current.operand3  # OP 3 
                # Allocates use 
                pr3 = self.vr_pr[op3[1]] 
                if pr3 == None: 
                    op3[2] = self.get_pr(op3[1], op3[3], current)
                    self.restore(op3[1], op3[2], current)
                else: 
                    op3[2] = pr3 
                self.marked[pr3] = 1
                # Last use 
                if op3[3] == float('inf') and self.pr_vr[op3[2]] != None: 
                    self.free_pr(op3[2])

                # Reset marks
                self.marked = list([0] * (self.num_regs - 2))
                if self.max_live <= self.num_regs: 
                    self.marked.append(0)
            elif current.spec_op == constants.LOAD: 
                # For use 
                op1 = current.operand1  # OP 1 
                # Allocates use 
                pr1 = self.vr_pr[op1[1]]
                if pr1 == None: 
                    op1 = self.get_pr(op1[1], op1[3], current)
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked[pr1] = 1
                # Last use 
                if op1[3] == float('inf') and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])

                # Reset marks
                self.marked = list([0] * (self.num_regs - 2))
                if self.max_live <= self.num_regs: 
                    self.marked.append(0)
                    
                # For definition
                op3 = current.operand3  # OP 3
                pr3 = self.get_pr(op3[1], op3[3], current)
                op3[2] = pr3
                self.marked[pr3] = 1
            elif current.opcode == constants.LOADI: 
                # For definition
                op3 = current.operand3  # OP 3
                pr3 = self.get_pr(op3[1], op3[3], current)
                op3[2] = pr3
                self.marked[pr3] = 1
            else: 
                # For use 
                op1 = current.operand1  # OP 1
                # Allocates use  
                pr1 = self.vr_pr[op1[1]]
                if pr1 == None: 
                    op1 = self.get_pr(op1[1], op1[3], current)
                    self.restore(op1[1], op1[2], current)
                else: 
                    op1[2] = pr1 
                self.marked[pr1] = 1
                # Last use 
                if op1[3] == float('inf') and self.pr_vr[op1[2]] != None: 
                    self.free_pr(op1[2])

                # For use 
                op2 = current.operand2  # OP 2 
                # Allocates use 
                pr2 = self.vr_pr[op2[1]]
                if pr2 == None: 
                    op2 = self.get_pr(op2[1], op2[3], current)
                    self.restore(op2[1], op2[2], current)
                else: 
                    op1[2] = pr2
                self.marked[pr2] = 1 
                # Last use 
                if op2[3] == float('inf') and self.pr_vr[op2[2]] != None: 
                    self.free_pr(op2[2])

                # Reset marks
                self.marked = list([0] * (self.num_regs - 2))
                if self.max_live <= self.num_regs: 
                    self.marked.append(0)

                # For definition
                op3 = current.operand3  # OP 3
                pr3 = self.get_pr(op3[1], op3[3], current)
                op3[2] = pr3
                self.marked[pr3] = 1
