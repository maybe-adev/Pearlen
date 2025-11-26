import sys
from interpreter.runner import run_program

VERSION = "Pearlen 0.1.1 Alpha"

def show_help():
    print("""
Pearlen CLI
Usage:
  pearl <file.pearl>        Run a Pearlen file
  pearl -i                  Interactive mode
  pearl -v                  Show version
    """)

def run_file(path):
    try:
        with open(path, "r") as f:
            code = f.read()
        run_program(code)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")

def repl():
    print("Pearlen REPL — type 'exit' to quit")
    while True:
        line = input("pearlen> ").strip()
        if line == "exit":
            break
        run_program(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    cmd = sys.argv[1]

    if cmd.endswith(".pearl"):
        run_file(cmd)

    elif cmd == "-i":
        repl()

    elif cmd == "-v":
        print(VERSION)

    else:
        show_help()
