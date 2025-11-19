import re

TOKEN_REGEX = [
    ("COMMENT_BLOCK", r"<.*?/>", re.DOTALL),
    ("COMMENT_LINE", r"#.*"),
    ("STRING", r"\"(.*?)\""),
    ("NUMBER", r"\d+(\.\d+)?"),
    ("IDENT", r"[a-zA-Z_]\w*"),
    ("OP", r"[+\-*/=()]"),
    ("NEWLINE", r"\n"),     # <-- IMPORTANT FIX
    ("SKIP", r"[ \t]+"),
]

def tokenize(code):
    tokens = []
    index = 0

    while index < len(code):
        matched = False

        for tok_type, pattern, *flags in TOKEN_REGEX:
            flag = flags[0] if flags else 0
            regex = re.compile(pattern, flag)
            match = regex.match(code, index)

            if match:
                matched = True
                value = match.group(0)

                # Ignore whitespace + comments + newlines
                if tok_type in ("COMMENT_BLOCK", "COMMENT_LINE", "NEWLINE", "SKIP"):
                    index = match.end()
                    break

                tokens.append((tok_type, value))
                index = match.end()
                break

        if not matched:
            raise SyntaxError(f"Unexpected character: {code[index]}")

    return tokens
