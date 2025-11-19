class Evaluator:
    def __init__(self):
        self.vars = {}

    def eval(self, tree):
        for stmt in tree:
            self.execute(stmt)

    def execute(self, stmt):
        stype = stmt[0]

        if stype == "ASSIGN":
            _, name, expr = stmt
            self.vars[name] = self.eval_expr(expr)

        elif stype == "SHOW":
            print(self.eval_expr(stmt[1]))

    def eval_expr(self, expr):
        etype = expr[0]

        if etype == "NUMBER":
            return expr[1]

        if etype == "STRING":
            return expr[1]

        if etype == "VAR":
            name = expr[1]
            if name not in self.vars:
                raise NameError(f"Variable '{name}' not defined")
            return self.vars[name]

        if etype == "BINOP":
            op, node1, node2 = expr[1], expr[2], expr[3]
            left = self.eval_expr(node1)
            right = self.eval_expr(node2)

            if op == "+": return left + right
            if op == "-": return left - right
            if op == "*": return left * right
            if op == "/": return left / right

        raise ValueError(f"Unknown expression type: {etype}")
