class Node: 

    def __init__(self, line_num, opcode, sr1, sr2, sr3):  
        self.line_num = line_num
        self.opcode = opcode
        self.sr1 = sr1
        self.sr2 = sr2
        self.sr3 = sr3
        self.next = None
        self.prev = None

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None

    def add(self, line_num, opcode, sr1, sr2, sr3): 
        new_node = Node(line_num, opcode, sr1, sr2, sr3)
        if not self.head: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail   
            self.tail = new_node
    
    def __str__(self):
        result = []
        current = self.head 
        while current: 
            result.append(f"[{current.line_num}: {current.opcode}, {current.sr1}, {current.sr2}, {current.sr3}]")
            current = current.next
        return " <-> ".join(result) + " <-> None"
            