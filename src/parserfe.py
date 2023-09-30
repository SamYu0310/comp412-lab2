import sys
from scanner import Scanner 
from intermediate_rep import DoublyLinkedList
import constants

class Parser: #build doubly linked list for IR 

    def __init__(self, file): 
        self.file = file
        self.word = 0
        self.line_num = 1
        self.parsed_lines = 0
        self.ir = DoublyLinkedList()

    def print_tokens(self): 
        scanner = Scanner(self.file)
        self.word = scanner.get_token()
        while self.word[0] != constants.EOF: 
            print(f"line number {self.line_num}: {self.word}")
            if self.word[0] == 11: 
                self.line_num += 1
            self.word = scanner.get_token()
        self.line_num = scanner.line_num
        print(f"line number {self.line_num}: {self.word}")

    def finish_memop(self, scanner): 
        opcode = self.word[0]
        spec_op = self.word[2]
        sr1 = 0
        sr3 = 0

        self.word = scanner.get_token()
        if self.word[0] == 7: 
            sr1 = int(self.word[1][1::])
            self.word = scanner.get_token()
            if self.word[0] == 9: 
                self.word = scanner.get_token()
                if self.word[0] == 7: 
                    sr3 = int(self.word[1][1::])
                    self.word = scanner.get_token()
                    if self.word[0] == 11: 
                        self.ir.add(self.line_num, opcode, sr1, None, sr3, spec_op)
                        self.parsed_lines += 1
                        self.line_num = scanner.line_num
                        self.word = scanner.get_token()
                    elif self.word[0] == 10: 
                        self.ir.add(self.line_num, opcode, sr1, None, sr3, spec_op)
                        self.parsed_lines += 1
                    else: 
                        if self.word[0] == 12: 
                            self.line_num = scanner.line_num
                        else: 
                            print(f"ERROR {self.line_num}: extra characters: should be end of line", file=sys.stderr)
                            self.line_num += 1
                else: 
                    if self.word[0] == 12: 
                        self.line_num = scanner.line_num
                    else: 
                        print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                        self.line_num += 1
            else: 
                if self.word[0] == 12: 
                    self.line_num = scanner.line_num
                else: 
                    print(f"ERROR {self.line_num}: missing =>", file=sys.stderr)
                    self.line_num += 1
        else: 
            if self.word[0] == 12: 
                self.line_num = scanner.line_num
            else: 
                print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                self.line_num += 1

    def finish_loadI(self, scanner): 
        opcode = self.word[0]
        spec_op = self.word[2]
        sr1 = 0
        sr3 = 0

        self.word = scanner.get_token()
        if self.word[0] == 6:
            sr1 = int(self.word[1])
            self.word = scanner.get_token()
            if self.word[0] == 9: 
                self.word = scanner.get_token()
                if self.word[0] == 7: 
                    sr3 = int(self.word[1][1::])
                    self.word = scanner.get_token()
                    if self.word[0] == 11: 
                        self.ir.add(self.line_num, opcode, sr1, None, sr3, spec_op)
                        self.parsed_lines += 1
                        self.line_num = scanner.line_num
                        self.word = scanner.get_token()
                    elif self.word[0] == 10: 
                        self.ir.add(self.line_num, opcode, sr1, None, sr3, spec_op)
                        self.parsed_lines += 1
                    else: 
                        if self.word[0] == 12: 
                            self.line_num = scanner.line_num
                        else: 
                            print(f"ERROR {self.line_num}: extra characters: should be end of line", file=sys.stderr)
                            self.line_num += 1
                else:
                    if self.word[0] == 12: 
                        self.line_num = scanner.line_num
                    else: 
                        print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                        self.line_num += 1
            else: 
                if self.word[0] == 12: 
                    self.line_num = scanner.line_num
                else: 
                    print(f"ERROR {self.line_num}: missing =>", file=sys.stderr)
                    self.line_num += 1
        else: 
            if self.word[0] == 12: 
                self.line_num = scanner.line_num
            else: 
                print(f"ERROR {self.line_num}: missing constant", file=sys.stderr)
                self.line_num += 1

    def finish_arithop(self, scanner): 
        opcode = self.word[0]
        spec_op = self.word[2]
        sr1 = 0
        sr2 = 0
        sr3 = 0

        self.word = scanner.get_token()
        if self.word[0] == 7: 
            sr1 = int(self.word[1][1::])
            self.word = scanner.get_token()
            if self.word[0] == 8: 
                self.word = scanner.get_token()
                if self.word[0] == 7: 
                    sr2 = int(self.word[1][1::])
                    self.word = scanner.get_token()
                    if self.word[0] == 9: 
                        self.word = scanner.get_token()
                        if self.word[0] == 7: 
                            sr3 = int(self.word[1][1::])
                            self.word = scanner.get_token()
                            if self.word[0] == 11: 
                                self.ir.add(self.line_num, opcode, sr1, sr2, sr3, spec_op)
                                self.parsed_lines += 1
                                self.line_num = scanner.line_num
                                self.word = scanner.get_token()
                            elif self.word[0] == 10: 
                                self.ir.add(self.line_num, opcode, sr1, sr2, sr3, spec_op)
                                self.parsed_lines += 1
                            else:
                                if self.word[0] == 12: 
                                    self.line_num = scanner.line_num
                                else: 
                                    print(f"ERROR {self.line_num}: extra characters: should be end of line", file=sys.stderr)
                                    self.line_num += 1
                        else: 
                            if self.word[0] == 12: 
                                self.line_num = scanner.line_num
                            else: 
                                print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                                self.line_num += 1
                    else:
                        if self.word[0] == 12: 
                            self.line_num = scanner.line_num
                        else: 
                            print(f"ERROR {self.line_num}: missing =>", file=sys.stderr)
                            self.line_num += 1
                else:
                    if self.word[0] == 12: 
                        self.line_num = scanner.line_num
                    else:  
                        print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                        self.line_num += 1
            else:
                if self.word[0] == 12: 
                    self.line_num = scanner.line_num
                else: 
                    print(f"ERROR {self.line_num}: missing comma", file=sys.stderr)
                    self.line_num += 1
        else:
            if self.word[0] == 12: 
                self.line_num = scanner.line_num
            else: 
                print(f"ERROR {self.line_num}: missing REG", file=sys.stderr)
                self.line_num += 1
    
    def finish_output(self, scanner): 
        opcode = self.word[0]
        spec_op = self.word[2]
        sr1 = 0

        self.word = scanner.get_token()
        if self.word[0] == 6: 
            sr1 = int(self.word[1])
            self.word = scanner.get_token()
            if self.word[0] == 11: 
                self.ir.add(self.line_num, opcode, sr1, None, None, spec_op)
                self.parsed_lines += 1
                self.line_num = scanner.line_num
                self.word = scanner.get_token()
            elif self.word[0] == 10: 
                self.ir.add(self.line_num, opcode, sr1, None, None, spec_op)
                self.parsed_lines += 1
            else:
                if self.word[0] == 12: 
                    self.line_num = scanner.line_num
                else: 
                    print(f"ERROR {self.line_num}: extra characters: should be end of line", file=sys.stderr)
                    self.line_num += 1
        else:
            if self.word[0] == 12: 
                self.line_num = scanner.line_num
            else: 
                print(f"ERROR {self.line_num}: missing constant", file=sys.stderr)
                self.line_num += 1

    def finish_nop(self, scanner): 
        opcode = self.word[0]
        spec_op = self.word[2]
        self.word = scanner.get_token()
        if self.word[0] == 11: 
            self.ir.add(self.line_num, opcode, None, None, None, spec_op)
            self.parsed_lines += 1
            self.line_num = scanner.line_num
            self.word = scanner.get_token()
        elif self.word[0] == 12: 
            self.ir.add(self.line_num, opcode, None, None, None, spec_op)
            self.parsed_lines += 1
        else:
            if self.word[0] == 12: 
                self.line_num = scanner.line_num
            else: 
                print(f"ERROR {self.line_num}: extra characters: should be end of line", file=sys.stderr)
                self.line_num += 1

    def parse(self): 
        scanner = Scanner(self.file)
        self.word = scanner.get_token()
        while self.word[0] != constants.EOF:
            if self.word[0] == 11 or self.word[0] == 12: 
                self.line_num = scanner.line_num
                self.word = scanner.get_token()
            elif self.word[0] == 1: 
                self.finish_memop(scanner)
            elif self.word[0] == 2: 
                self.finish_loadI(scanner)
            elif self.word[0] == 3: 
                self.finish_arithop(scanner)
            elif self.word[0] == 4: 
                self.finish_output(scanner)
            elif self.word[0] == 5: 
                self.finish_nop(scanner)
            else:
                self.line_num = scanner.line_num
                self.word = scanner.get_token()

        if constants.PFLAG: 
            return(f"Successfully parsed {self.parsed_lines} line(s)")
        elif constants.RFLAG: 
            return self.ir
        else: 
            return("Done!")
