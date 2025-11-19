vars = {}

def eval_expr(expr):
    for name, value in vars.items():
        expr = expr.replace(name, str(value))
    return eval(expr)
