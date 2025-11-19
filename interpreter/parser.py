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
            statements.append(self.statement())
        return statements

    # ----------------------------
    # STATEMENTS
    # ----------------------------
    def statement(self):
        tok_type, tok_val = self.peek()

        if tok_type == "IDENT" and tok_val == "show":
            return self.show_stmt()

        if tok_type == "IDENT":
            return self.assign_stmt()

        raise SyntaxError(f"Unexpected token: {tok_val}")

    def assign_stmt(self):
        name = self.eat("IDENT")[1]
        self.eat("OP", "=")
        expr = self.expr()
        return ("ASSIGN", name, expr)

    def show_stmt(self):
        self.eat("IDENT")      # show
        self.eat("OP", "(")
        expr = self.expr()
        self.eat("OP", ")")
        return ("SHOW", expr)

    # ----------------------------
    # EXPRESSIONS (supports + - * / and parentheses)
    # ----------------------------

    def expr(self):
        node = self.term()
        while True:
            tok = self.peek()
            if tok[0] == "OP" and tok[1] in ("+", "-"):
                op = self.eat("OP")[1]
                right = self.term()
                node = ("BINOP", op, node, right)
            else:
                break
        return node

    def term(self):
        node = self.factor()
        while True:
            tok = self.peek()
            if tok[0] == "OP" and tok[1] in ("*", "/"):
                op = self.eat("OP")[1]
                right = self.factor()
                node = ("BINOP", op, node, right)
            else:
                break
        return node

    def factor(self):
        tok_type, tok_val = self.peek()

        if tok_type == "NUMBER":
            return ("NUMBER", float(self.eat("NUMBER")[1]))

        if tok_type == "STRING":
            return ("STRING", self.eat("STRING")[1][1:-1])

        if tok_type == "IDENT":
            return ("VAR", self.eat("IDENT")[1])

        if tok_type == "OP" and tok_val == "(":
            self.eat("OP", "(")
            node = self.expr()
            self.eat("OP", ")")
            return node

        raise SyntaxError(f"Unexpected expression token: {tok_val}")
