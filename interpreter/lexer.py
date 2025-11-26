import re

TOKEN_REGEX = [
    ("COMMENT_BLOCK", r"<.*?/>", re.DOTALL),
    ("COMMENT_LINE", r"#.*"),
    ("STRING", r"\"(.*?)\""),
    ("NUMBER", r"\d+(\.\d+)?"),

    # Comparison operators
    ("EQEQ", r"=="),
    ("NOTEQ", r"!="),
    ("LTE", r"<="),
    ("GTE", r">="),
    ("LT", r"<"),
    ("GT", r">"),

    # Arithmetic
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MUL", r"\*"),
    ("DIV", r"/"),
    ("ASSIGN", r"="),

    # Symbols
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COLON", r":"),

    # Identifiers
    ("IDENT", r"[a-zA-Z_]\w*"),

    ("SKIP", r"[ \t]+"),
]

KEYWORDS = {
    "if": "IF",
    "else": "ELSE",
    "end": "END",
    "show": "SHOW",
    "switch": "SWITCH",
    "option": "OPTION",
    "default": "DEFAULT",
    "then": "THEN",
}

def tokenize(code):
    tokens = []
    indent_stack = [0]
    lines = code.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    for line in lines:
        stripped = line.lstrip()
        if stripped == "":
            tokens.append(("NEWLINE", "\n"))
            continue

        indent = len(line) - len(stripped)
        if indent > indent_stack[-1]:
            indent_stack.append(indent)
            tokens.append(("INDENT", None))
        while indent < indent_stack[-1]:
            indent_stack.pop()
            tokens.append(("DEDENT", None))

        index = 0
        while index < len(stripped):
            matched = False
            for tok_type, pattern, *flags in TOKEN_REGEX:
                flag = flags[0] if flags else 0
                regex = re.compile(pattern, flag)
                match = regex.match(stripped, index)
                if match:
                    matched = True
                    value = match.group(0)
                    if tok_type in ("COMMENT_BLOCK", "COMMENT_LINE", "SKIP"):
                        index = match.end()
                        break
                    if tok_type == "IDENT" and value in KEYWORDS:
                        tokens.append((KEYWORDS[value], value))
                    else:
                        tokens.append((tok_type, value))
                    index = match.end()
                    break
            if not matched:
                raise SyntaxError(f"Unexpected character: {stripped[index]!r}")
        tokens.append(("NEWLINE", "\n"))

    while len(indent_stack) > 1:
        indent_stack.pop()
        tokens.append(("DEDENT", None))

    return tokens
