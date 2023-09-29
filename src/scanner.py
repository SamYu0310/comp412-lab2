import sys 
import constants

class Scanner: 

    def __init__(self, file): 
        self.file = file
        self.line = file.readline()
        self.line_num = 1
        self.position = 0 
        self.lexeme = ""

    def get_token(self): 
        if self.line == "":
            return (constants.EOF, "")
        if self.line[-1] != '\n': 
            self.line += "\n"
        c = self.line[self.position]
        if c == ' ' or c == '\t': 
            while c == ' ' or c == '\t': 
                self.position += 1
                c = self.line[self.position]
        if c == '/': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == '/': 
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return (constants.EOL, "\n")
            else: 
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == '\n': 
            self.position = 0
            self.lexeme = ""
            self.line = self.file.readline()
            self.line_num += 1
            return (constants.EOL, "\n")
        elif c == 'a': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 'd': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'd': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == ' ' or c == '\t': 
                        self.position += 1
                        token = (constants.ARITHOP, self.lexeme)
                        self.lexeme = ""
                        return token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else:
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 'l':  
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position] 
            if c == 'o': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'a': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == 'd': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == 'I': 
                            self.lexeme += self.line[self.position]
                            self.position += 1
                            c = self.line[self.position]
                            if c == ' ' or c == '\t': 
                                self.position += 1
                                token = (constants.LOADI, self.lexeme)
                                self.lexeme = ""
                                return token
                            else:
                                self.lexeme += c 
                                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                error_token = (constants.ERROR, self.lexeme)
                                self.position = 0
                                self.lexeme = ""
                                self.line = self.file.readline()
                                self.line_num += 1
                                return error_token
                        elif c == ' ' or c == '\t': 
                            self.position += 1
                            token = (constants.MEMOP, self.lexeme)
                            self.lexeme = ""
                            return token
                        else: 
                            self.lexeme += c
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            elif c == 's': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'h': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position] 
                    if c == 'i': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == 'f': 
                            self.lexeme += self.line[self.position]
                            self.position += 1
                            c = self.line[self.position]
                            if c == 't': 
                                self.lexeme += self.line[self.position]
                                self.position += 1
                                c = self.line[self.position]
                                if c == ' ' or c == '\t': 
                                    self.position += 1
                                    token = (constants.ARITHOP, self.lexeme)
                                    self.lexeme = ""
                                    return token
                                else:
                                    self.lexeme += c 
                                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                    error_token = (constants.ERROR, self.lexeme)
                                    self.position = 0
                                    self.lexeme = ""
                                    self.line = self.file.readline()
                                    self.line_num += 1
                                    return error_token
                            else: 
                                self.lexeme += c
                                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                error_token = (constants.ERROR, self.lexeme)
                                self.position = 0
                                self.lexeme = ""
                                self.line = self.file.readline()
                                self.line_num += 1
                                return error_token
                        else: 
                            self.lexeme += c
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 's': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 't': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'o': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == 'r': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == 'e': 
                            self.lexeme += self.line[self.position]
                            self.position += 1
                            c = self.line[self.position]
                            if c == ' ' or c == '\t': 
                                self.position += 1
                                token = (constants.MEMOP, self.lexeme)
                                self.lexeme = ""
                                return token 
                            else: 
                                self.lexeme += c
                                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                error_token = (constants.ERROR, self.lexeme)
                                self.position = 0
                                self.lexeme = ""
                                self.line = self.file.readline()
                                self.line_num += 1
                                return error_token
                        else: 
                            self.lexeme += c
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            elif c == 'u': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'b': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == ' ' or c == '\t': 
                        self.position += 1
                        token = (constants.ARITHOP, self.lexeme)
                        self.lexeme = ""
                        return token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 'r': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 's': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'h': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == 'i': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == 'f': 
                            self.lexeme += self.line[self.position]
                            self.position += 1
                            c = self.line[self.position]
                            if c == 't': 
                                self.lexeme += self.line[self.position]
                                self.position += 1
                                c = self.line[self.position]
                                if c == ' ' or c == '\t': 
                                    self.position += 1
                                    token = (constants.ARITHOP, self.lexeme)
                                    self.lexeme = ""
                                    return token
                                else: 
                                    self.lexeme += c
                                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                    error_token = (constants.ERROR, self.lexeme)
                                    self.position = 0
                                    self.lexeme = ""
                                    self.line = self.file.readline()
                                    self.line_num += 1
                                    return error_token
                            else: 
                                self.lexeme += c
                                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                error_token = (constants.ERROR, self.lexeme)
                                self.position = 0
                                self.lexeme = ""
                                self.line = self.file.readline()
                                self.line_num += 1
                                return error_token
                        else:
                            self.lexeme += c 
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            elif c.isdigit():
                while c.isdigit(): 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                token = (constants.REGISTER, self.lexeme)
                self.lexeme = ""
                return token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 'm': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 'u': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'l': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == 't': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == ' ' or c == '\t': 
                            self.position += 1
                            token = (constants.ARITHOP, self.lexeme)
                            self.lexeme = ""
                            return token
                        else: 
                            self.lexeme += c
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 'n': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 'o': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 'p': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == ' ' or c == '\t': 
                        self.position += 1
                        token = (constants.NOP, self.lexeme)
                        self.lexeme = ""
                        return token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == 'o': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == 'u': 
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
                if c == 't': 
                    self.lexeme += self.line[self.position]
                    self.position += 1
                    c = self.line[self.position]
                    if c == 'p': 
                        self.lexeme += self.line[self.position]
                        self.position += 1
                        c = self.line[self.position]
                        if c == 'u': 
                            self.lexeme += self.line[self.position]
                            self.position += 1
                            c = self.line[self.position]
                            if c == 't': 
                                self.lexeme += self.line[self.position]
                                self.position += 1
                                c = self.line[self.position]
                                if c == ' ' or c == '\t': 
                                    self.position += 1
                                    token = (constants.OUTPUT, self.lexeme)
                                    self.lexeme = ""
                                    return token
                                else: 
                                    self.lexeme += c
                                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                    error_token = (constants.ERROR, self.lexeme)
                                    self.position = 0
                                    self.lexeme = ""
                                    self.line = self.file.readline()
                                    self.line_num += 1
                                    return error_token
                            else: 
                                self.lexeme += c
                                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                                error_token = (constants.ERROR, self.lexeme)
                                self.position = 0
                                self.lexeme = ""
                                self.line = self.file.readline()
                                self.line_num += 1
                                return error_token
                        else: 
                            self.lexeme += c
                            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                            error_token = (constants.ERROR, self.lexeme)
                            self.position = 0
                            self.lexeme = ""
                            self.line = self.file.readline()
                            self.line_num += 1
                            return error_token
                    else: 
                        self.lexeme += c
                        print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                        error_token = (constants.ERROR, self.lexeme)
                        self.position = 0
                        self.lexeme = ""
                        self.line = self.file.readline()
                        self.line_num += 1
                        return error_token
                else: 
                    self.lexeme += c
                    print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                    error_token = (constants.ERROR, self.lexeme)
                    self.position = 0
                    self.lexeme = ""
                    self.line = self.file.readline()
                    self.line_num += 1
                    return error_token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == '=': 
            self.lexeme += self.line[self.position]
            self.position += 1
            c = self.line[self.position]
            if c == '>': 
                self.lexeme += self.line[self.position]
                self.position += 1
                token = (constants.INTO, self.lexeme)
                self.lexeme = ""
                return token
            else: 
                self.lexeme += c
                print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
                error_token = (constants.ERROR, self.lexeme)
                self.position = 0
                self.lexeme = ""
                self.line = self.file.readline()
                self.line_num += 1
                return error_token
        elif c == ',': 
            self.lexeme += self.line[self.position]
            self.position += 1
            token = (constants.COMMA, self.lexeme)
            self.lexeme = ""
            return token
        elif c.isdigit(): 
            while c.isdigit():
                self.lexeme += self.line[self.position]
                self.position += 1
                c = self.line[self.position]
            token = (constants.CONSTANT, self.lexeme)
            self.lexeme = ""
            return token
        else: 
            self.lexeme += c
            print(f"ERROR {self.line_num}: {self.lexeme} is not a valid word", file=sys.stderr)
            error_token = (constants.ERROR, self.lexeme)
            self.position = 0
            self.lexeme = ""
            self.line = self.file.readline()
            self.line_num += 1
            return error_token
                    

        

