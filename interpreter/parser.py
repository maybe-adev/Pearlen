class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def eat(self, kind=None, value=None):
        tok = self.peek()
        if kind and tok[0] != kind:
            raise SyntaxError(f"Expected {kind} but got {tok}")
        if value and tok[1] != value:
            raise SyntaxError(f"Expected {value} but got {tok}")
        self.pos += 1
        return tok

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
        return statements

    def statement(self):
        tok_type, tok_val = self.peek()
        if tok_type is None:
            return None
        if tok_type in ("NEWLINE", "DEDENT"):
            self.eat(tok_type)
            return self.statement()
        if tok_type == "IF":
            return self.if_stmt()
        if tok_type == "SWITCH":
            return self.switch_stmt()
        if tok_type == "SHOW":
            return self.show_stmt()
        if tok_type == "IDENT":
            return self.assign_stmt()
        if tok_type == "ELSE":
            raise SyntaxError("Unexpected 'else' outside if-block")
        raise SyntaxError(f"Unexpected token: {tok_type} {tok_val}")

    # ------------------- IF / ELSE THEN IF / ELSE -------------------
    def if_stmt(self):
        self.eat("IF")
        condition = self.expr()
        self.eat("COLON")
        self.eat("NEWLINE")
        self.eat("INDENT")
        then_block = self.block()
        self.eat("DEDENT")

        branches = [(condition, then_block)]

        while True:
            tok_type, _ = self.peek()
            if tok_type != "ELSE":
                break
            self.eat("ELSE")
            tok_type2, tok_val2 = self.peek()

            if tok_type2 == "THEN":
                self.eat("THEN")
                if self.peek()[0] != "IF":
                    raise SyntaxError("Expected 'if' after 'else then'")
                self.eat("IF")

                # Optional condition
                cond_tok_type, _ = self.peek()
                if cond_tok_type != "COLON":
                    nested_condition = self.expr()
                else:
                    nested_condition = None

                self.eat("COLON")
                self.eat("NEWLINE")
                self.eat("INDENT")
                nested_block = self.block()
                self.eat("DEDENT")
                branches.append((nested_condition, nested_block))
            else:
                # else
                self.eat("COLON")
                self.eat("NEWLINE")
                self.eat("INDENT")
                else_block = self.block()
                self.eat("DEDENT")
                branches.append((None, else_block))
                break

        self.eat("END")
        self.eat("NEWLINE")

        # Build nested AST
        ast = None
        for cond, blk in reversed(branches):
            if ast is None:
                ast = ("IF", cond, blk, None)
            else:
                ast = ("IF", cond, blk, [ast])
        return ast

    # ------------------- SWITCH / OPTION / DEFAULT -------------------
  
    def switch_stmt(self):
        self.eat("SWITCH")
        expr = self.expr()
        self.eat("COLON")
        self.eat("NEWLINE")
        self.eat("INDENT")
    
        cases = []
        default_block = None
    
        while True:
            tok_type, tok_val = self.peek()
            if tok_type == "OPTION":
                self.eat("OPTION")
                value = self.expr()
                self.eat("COLON")
                self.eat("NEWLINE")
                self.eat("INDENT")
                block = self.block()
                self.eat("DEDENT")
                cases.append((value, block))
            elif tok_type == "DEFAULT":
                self.eat("DEFAULT")
                self.eat("COLON")
                self.eat("NEWLINE")
                self.eat("INDENT")
                default_block = self.block()
                self.eat("DEDENT")
            else:
                break
    
        # Consume any DEDENTs before END
        while self.peek()[0] == "DEDENT":
            self.eat("DEDENT")
    
        self.eat("END")
        self.eat("NEWLINE")
    
        return ("SWITCH", expr, cases, default_block)


    def block(self):
        statements = []
        while True:
            tok_type, _ = self.peek()
            if tok_type in ("DEDENT", "END", None):
                break
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
        return statements

    def show_stmt(self):
        self.eat("SHOW")
        self.eat("LPAREN")
        expr = self.expr()
        self.eat("RPAREN")
        if self.peek()[0] == "NEWLINE":
            self.eat("NEWLINE")
        return ("SHOW", expr)

    def assign_stmt(self):
        name = self.eat("IDENT")[1]
        self.eat("ASSIGN")
        expr = self.expr()
        if self.peek()[0] == "NEWLINE":
            self.eat("NEWLINE")
        return ("ASSIGN", name, expr)

    # ------------------- Expressions -------------------
    def expr(self):
        return self.compare()

    def compare(self):
        node = self.term()
        while True:
            tok_type, _ = self.peek()
            if tok_type in ("EQEQ", "NOTEQ", "LT", "LTE", "GT", "GTE"):
                op = self.eat(tok_type)[1]
                right = self.term()
                node = ("COMPARE", op, node, right)
            else:
                break
        return node

    def term(self):
        node = self.factor()
        while True:
            tok_type, _ = self.peek()
            if tok_type in ("PLUS", "MINUS"):
                op = self.eat(tok_type)[1]
                right = self.factor()
                node = ("BINOP", op, node, right)
            else:
                break
        return node

    def factor(self):
        node = self.atom()
        while True:
            tok_type, _ = self.peek()
            if tok_type in ("MUL", "DIV"):
                op = self.eat(tok_type)[1]
                right = self.atom()
                node = ("BINOP", op, node, right)
            else:
                break
        return node

    def atom(self):
        tok_type, tok_val = self.peek()
        if tok_type == "NUMBER":
            return ("NUMBER", float(self.eat("NUMBER")[1]))
        if tok_type == "STRING":
            return ("STRING", self.eat("STRING")[1][1:-1])
        if tok_type == "IDENT":
            return ("VAR", self.eat("IDENT")[1])
        if tok_type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node
        raise SyntaxError(f"Unexpected token in expression: {tok_type} {tok_val}")
