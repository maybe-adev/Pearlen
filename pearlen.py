import sys

VERSION = "Pearlen 0.1.0 Alpha"

# ----------------------------------
# INTERPRETER CORE
# ----------------------------------

vars = {}

def eval_expr(expr):
    for name, value in vars.items():
        expr = expr.replace(name, str(value))
    return eval(expr)

def run_line(line):
    line = line.strip()

    if "=" in line and not line.startswith("if") and not line.startswith("loop"):
        name, expr = line.split("=", 1)
        vars[name.strip()] = eval_expr(expr.strip())
        return

    if line.startswith("show(") and line.endswith(")"):
        print(eval_expr(line[5:-1]))
        return

    if line.startswith("print(") and line.endswith(")"):
        print(eval_expr(line[6:-1]))
        return

    return line


def run_program(code):
    lines = code.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # IF
        if line.startswith("if "):
            condition = line[3:].strip()[:-1]
            cond_val = eval_expr(condition)

            block = []
            i += 1

            while i < len(lines) and lines[i].strip() not in ("else:", "end"):
                block.append(lines[i])
                i += 1

            if cond_val:
                for b in block:
                    run_line(b)
            else:
                if i < len(lines) and lines[i].strip() == "else:":
                    i += 1
                    else_block = []
                    while i < len(lines) and lines[i].strip() != "end":
                        else_block.append(lines[i])
                        i += 1
                    for b in else_block:
                        run_line(b)

            while i < len(lines) and lines[i].strip() != "end":
                i += 1

        # LOOP
        elif line.startswith("loop "):
            count = eval_expr(line[5:].strip()[:-1])
            block = []

            i += 1
            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1

            for _ in range(int(count)):
                for b in block:
                    run_line(b)

        else:
            run_line(line)

        i += 1


# ----------------------------------
# CLI COMMANDS
# ----------------------------------

def show_help():
    print("""
Pearlen CLI 0.1.0 Alpha
Usage:
  pearlen run <file.pearl>   Run a Pearlen file
  pearlen repl               Start interactive mode
  pearlen version            Show version
    """)


def run_file(path):
    try:
        with open(path, "r") as f:
            code = f.read()
        run_program(code)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
    except Exception as e:
        print("Runtime Error:", e)


def repl():
    print("Pearlen REPL — type 'exit' to quit\n")
    while True:
        line = input("pearlen> ").strip()
        if line == "exit":
            break
        try:
            if line.startswith("show(") or "=" in line:
                run_line(line)
            else:
                print("Only 'show()' and simple expressions allowed in REPL for now.")
        except Exception as e:
            print("Error:", e)


# ----------------------------------
# MAIN ENTRY
# ----------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    cmd = sys.argv[1]

    if cmd == "run":
        if len(sys.argv) < 3:
            print("Error: No file provided.\nUsage: pearlen run file.pearl")
        else:
            run_file(sys.argv[2])

    elif cmd == "repl":
        repl()

    elif cmd == "version":
        print(VERSION)

    else:
        show_help()
