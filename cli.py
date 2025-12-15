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
    if not path.endswith(".pearl"):
        print_error("only .pearl files are supported.")
        return

    try:
        with open(path, "r") as f:
            code = f.read()
        run_program(code)
    except FileNotFoundError:
        print_error(f"file '{path}' not found.")
    except (SyntaxError, ValueError, NameError) as e:
        print_error(str(e))
    except Exception as e:
        print_error(f"an unexpected error occurred: {e}")

def repl():
    print("Pearlen REPL — type 'exit' to quit")
    while True:
        try:
            line = input("pearlen> ").strip()
            if line == "exit":
                break
            run_program(line)
            if line == "":
                continue
        # Handling Ctrl + D on Mac/Linux or Ctrl + Z on Windows then Enter
        except EOFError:
            print("\nExiting Pearlen REPL.")
            break
        except (SyntaxError, ValueError, NameError) as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"an unexpected error occurred: {e}")

def print_error(message):
    print(f"Error: {message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd.endswith(".pearl"):
        run_file(cmd)

    elif cmd == "-i":
        repl()

    elif cmd == "-v":
        print(VERSION)

    else:
        show_help()
