<p align="center">
██████╗ ███████╗ █████╗ ██████╗ ██╗     ███████╗███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝████╗  ██║
██████╔╝█████╗  ███████║██████╔╝██║     █████╗  ██╔██╗ ██║
██╔══██╗██╔══╝  ██╔══██║██╔══██╗██║     ██╔══╝  ██║╚██╗██║
██║  ██║███████╗██║  ██║██║  ██║███████╗███████╗██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
</p>

# 🌟 Pearlen — A Mini Programming Language
<p align="center">
  <img src="https://img.shields.io/badge/Pearlen-Language-4C4CFF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/version-0.1.0_Alpha-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20With-Python-3670A0?style=for-the-badge&logo=python&logoColor=yellow" />
  <img src="https://img.shields.io/badge/license-MIT-black?style=for-the-badge" />
</p>

## 🚀 Features

- 📌 Variable declarations and assignments  
- 🧮 Arithmetic expressions  
- 🖨️ `print()` for output  
- 📝 Strings (double quotes `" "`)  
- 💬 Two types of comments:
  - `< This is a block comment />`
  - `# This is a line comment`

---

## 📁 Project Structure

```

Pearlen/
│
├── cli.py                  # Main CLI entry point
├── README.md
├── examples/               # Sample .pearl programs
│   ├── basics.pearl
│   ├── comments.pearl
│   ├── strings.pearl
│
└── interpreter/
├── lexer.py            # Tokenizer
├── parser.py           # AST builder
├── evaluator.py        # Expression evaluator
└── runner.py           # Executes final AST

````

---

## ▶️ How to Run

Run any `.pearl` file using:

```sh
pearl examples/basics.pearl
````

Or directly with Python:

```sh
python cli.py examples/basics.pearl
```

---

## 📚 Example Programs

### 1️⃣ basics.pearl

```pearl
print("Hello from Pearlen")

x = 10
y = 20

print(x + y)
```

---

### 2️⃣ comments.pearl

```pearl
# This is a line comment
print("Line comment works")

< This is a block comment />
print("Block comment works")

# Mixing comments
< Pearlen Language />
print("Both comments running fine")
```

---

### 3️⃣ strings.pearl

```pearl
message = "Pearlen is fun!"
name = "Ayush"

print(message)
print("Hello " + name)

# String concatenation
print("A" + "B" + "C")
```

---

## 💡 Comment Syntax

### ✔ Block Comment

```pearl
< This is a block comment />
```

Ignored by the lexer.

### ✔ Line Comment

```pearl
# Everything after this symbol is ignored
```

---

## 🧠 Future Features (Planned)

* Conditionals (`if / else`)
* Loops (`while`)
* Functions
* Imports
* Standard Library

---

## 🧩 Contributing

Pull requests and feature ideas are welcome!
If you want help implementing new features, just ask.

---

## ⭐ License

MIT License — free to use, modify, and learn from.

