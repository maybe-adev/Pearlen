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

        elif stype == "IF":
            _, condition, then_block, else_block = stmt

            if condition is None:
                for s in then_block:
                    self.execute(s)
            else:
                if self.eval_expr(condition):
                    for s in then_block:
                        self.execute(s)
                elif else_block:
                    for s in else_block:
                        self.execute(s)

        elif stype == "SWITCH":
            _, expr, cases, default_block = stmt
            val = self.eval_expr(expr)
            matched = False
            for case_val_expr, block in cases:
                if self.eval_expr(case_val_expr) == val:
                    for s in block:
                        self.execute(s)
                    matched = True
                    break
            if not matched and default_block:
                for s in default_block:
                    self.execute(s)

        else:
            raise ValueError(f"Unknown statement type: {stype}")

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
            op, left_node, right_node = expr[1], expr[2], expr[3]
            left = self.eval_expr(left_node)
            right = self.eval_expr(right_node)
            if op == "+": return left + right
            if op == "-": return left - right
            if op == "*": return left * right
            if op == "/": return left / right
            raise ValueError(f"Unknown BINOP {op}")

        if etype == "COMPARE":
            op, left_node, right_node = expr[1], expr[2], expr[3]
            left = self.eval_expr(left_node)
            right = self.eval_expr(right_node)
            if op == "<": return left < right
            if op == "<=": return left <= right
            if op == ">": return left > right
            if op == ">=": return left >= right
            if op == "==": return left == right
            if op == "!=": return left != right
            raise ValueError(f"Unknown COMPARE {op}")

        raise ValueError(f"Unknown expression type: {etype}")
