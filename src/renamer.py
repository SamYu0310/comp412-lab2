from intermediate_rep import DoublyLinkedList

class Renamer: 

    def __init__(self, ir: DoublyLinkedList): 
        self.ir = ir

    def rename(self): 
        vr_name = 0
        sr_vr = [None] * (self.ir.max_sr + 1)
        lu = [float('inf')] * (self.ir.max_sr + 1)
        index = self.ir.num_nodes
        current = self.ir.tail
        while current: 
            if current.opcode == 4 or current.opcode == 5: 
                continue 
            elif current.spec_op == 13: 
                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = vr_name
                    vr_name += 1
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 
                
                op3 = current.operand3 
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = vr_name
                    vr_name += 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                lu[op3[0]] = index 

                index -= 1
            elif current.spec_op == 14: 
                # For operand that is defined  
                op3 = current.operand3
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = vr_name
                    vr_name += 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')

                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = vr_name
                    vr_name += 1
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 
            elif current.opcode == 2: 
                # For operand that is defined 
                op3 = current.operand3 
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = vr_name
                    vr_name += 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')
            else: 
                # For operand that is defined  
                op3 = current.operand3
                if sr_vr[op3[0]] == None: 
                    sr_vr[op3[0]] = vr_name
                    vr_name += 1
                op3[1] = sr_vr[op3[0]]
                op3[3] = lu[op3[0]]
                sr_vr[op3[0]] = None 
                lu[op3[0]] = float('inf')

                # For operand that is used 
                op1 = current.operand1
                if sr_vr[op1[0]] == None: 
                    sr_vr[op1[0]] = vr_name
                    vr_name += 1
                op1[1] = sr_vr[op1[0]]
                op1[3] = lu[op1[0]]
                lu[op1[0]] = index 

                op2 = current.operand2
                if sr_vr[op2[0]] == None: 
                    sr_vr[op2[0]] = vr_name
                    vr_name += 1
                op2[1] = sr_vr[op2[0]]
                op2[3] = lu[op2[0]]
                lu[op2[0]] = index 
            index -= 1
            current = current.prev
            