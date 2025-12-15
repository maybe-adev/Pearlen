from interpreter.lexer import tokenize
from interpreter.parser import Parser
from interpreter.evaluator import Evaluator

def run_program(code):
    try:
        tokens = tokenize(code)
        parser = Parser(tokens)
        tree = parser.parse()
        evaluator = Evaluator()
        evaluator.eval(tree)
    except (SyntaxError, ValueError, NameError):
        raise
    except Exception as e:
        raise RuntimeError("an unexpected error occurred") from e

def run_line(line):
    run_program(line)
