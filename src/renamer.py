from intermediate_rep import DoublyLinkedList
import constants

class Renamer: 

    def __init__(self, ir: DoublyLinkedList): 
        self.ir = ir
        self.max_live = 0
        self.vr_name = 0

    def rename(self): 
        curr_live = 0
        sr_vr = [None] * (self.ir.max_sr + 1)
        lu = [float('inf')] * (self.ir.max_sr + 1)
        index = self.ir.num_nodes
        current = self.ir.tail
        while current: 
            if current.opcode == constants.OUTPUT or current.opcode == constants.NOP: 
                current = current.prev 
                continue 
            elif current.spec_op == constants.STORE: 
                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = self.vr_name
                    self.vr_name += 1
                    curr_live += 1
                    if curr_live > self.max_live: 
                        self.max_live = curr_live 
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 
                
                op3 = current.operand3 
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = self.vr_name
                    self.vr_name += 1
                    curr_live += 1
                    if curr_live > self.max_live: 
                        self.max_live = curr_live 
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                lu[op3[0]] = index 

                index -= 1
            elif current.spec_op == constants.LOAD: 
                # For operand that is defined  
                op3 = current.operand3
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = self.vr_name
                    self.vr_name += 1
                else:
                    curr_live -= 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')

                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = self.vr_name
                    self.vr_name += 1
                    curr_live += 1
                    if curr_live > self.max_live: 
                        self.max_live = curr_live 
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 
            elif current.opcode == constants.LOADI: 
                # For operand that is defined 
                op3 = current.operand3 
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = self.vr_name
                    self.vr_name += 1
                else: 
                    curr_live -= 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')
            else: 
                # For operand that is defined  
                op3 = current.operand3
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = self.vr_name
                    self.vr_name += 1
                else: 
                    curr_live -= 1 
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')

                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = self.vr_name
                    self.vr_name += 1
                    curr_live += 1
                    if curr_live > self.max_live: 
                        self.max_live = curr_live 
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 

                op2 = current.operand2
                if sr_vr[op2[0]] == None: 
                    sr_vr[op2[0]] = self.vr_name
                    self.vr_name += 1
                    curr_live += 1
                    if curr_live > self.max_live: 
                        self.max_live = curr_live 
                op2[1] = sr_vr[op2[0]]
                op2[3] = lu[op2[0]]
                lu[op2[0]] = index 

            # if curr_live > self.max_live: 
            #     self.max_live = curr_live 

            index -= 1
            current = current.prev

    def format(self): 
        current = self.ir.head
        while current: 
            if current.spec_op == constants.STORE: 
                print(f"store r{current.operand1[1]} => r{current.operand3[1]}")
            elif current.spec_op == constants.LOAD: 
                print(f"load r{current.operand1[1]} => r{current.operand3[1]}")         
            elif current.opcode == constants.LOADI: 
                print(f"loadI {current.operand1[0]} => r{current.operand3[1]}")
            elif current.spec_op == constants.ADD: 
                print(f"add r{current.operand1[1]}, r{current.operand2[1]} => r{current.operand3[1]}")
            elif current.spec_op == constants.SUB: 
                print(f"sub r{current.operand1[1]}, r{current.operand2[1]} => r{current.operand3[1]}")
            elif current.spec_op == constants.MULT: 
                print(f"mult r{current.operand1[1]}, r{current.operand2[1]} => r{current.operand3[1]}")
            elif current.spec_op == constants.LSHIFT: 
                print(f"lshift r{current.operand1[1]}, r{current.operand2[1]} => r{current.operand3[1]}")
            elif current.spec_op == constants.RSHIFT: 
                print(f"rshift r{current.operand1[1]}, r{current.operand2[1]} => r{current.operand3[1]}")
            elif current.opcode == constants.OUTPUT: 
                print(f"output {current.operand1[0]}")
            else: 
                print(f"nop")
            current = current.next 
