class Node: 

    def __init__(self, line_num, opcode, sr1, sr2, sr3, spec_op):  
        self.line_num = line_num
        self.opcode = opcode
        self.spec_op = spec_op
        self.operand1 = [sr1, None, None, None]  # SR, VR, PR, NU
        self.operand2 = [sr2, None, None, None]
        self.operand3 = [sr3, None, None, None]
        self.next = None
        self.prev = None

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None
        self.num_nodes = 0
        self.max_sr = 0

    def add(self, line_num, opcode, sr1, sr2, sr3, spec_op): 
        new_node = Node(line_num, opcode, sr1, sr2, sr3, spec_op)
        if not self.head: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail   
            self.tail = new_node
        self.num_nodes += 1
        if opcode == 4 or opcode == 5: 
            pass 
        elif opcode == 3: # 3 registers 
            if self.max_sr < max(sr1, sr2, sr3): 
                self.max_sr = max(sr1, sr2, sr3)
        elif opcode == 1: 
            if self.max_sr < max(sr1, sr3): 
                self.max_sr = max(sr1, sr3)
        else: 
            if self.max_sr < sr3: 
                self.max_sr = sr3
    
    def __str__(self):
        result = []
        current = self.head 
        while current: 
            result.append(f"[{current.line_num}: {current.opcode}, {current.sr1}, {current.sr2}, {current.sr3}]")
            current = current.next
        return " <-> ".join(result) + " <-> None"
