from interpreter.lexer import tokenize
from interpreter.parser import Parser
from interpreter.evaluator import Evaluator

def run_program(code):
    tokens = tokenize(code)
    parser = Parser(tokens)
    tree = parser.parse()
    evaluator = Evaluator()
    evaluator.eval(tree)

def run_line(line):
    run_program(line)
