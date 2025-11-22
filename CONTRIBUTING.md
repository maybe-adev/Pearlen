# ![Pearlen](https://img.shields.io/badge/Pearlen-Language-blueviolet) Contributing to **Pearlen Language**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Rust](https://img.shields.io/badge/Rust-parser-orange)](#)
[![Python](https://img.shields.io/badge/Python-interpreter-blue)](#)
[![License](https://img.shields.io/badge/license-Apache%202.0-black)](#)

Pearlen is a mini programming-language project using:

* **Python** → Interpreter + Lexer + Parser + Execution Engine + CLI

We welcome contributions of all kinds!
This guide explains how to report issues, submit patches, propose features, and help improve documentation.

---

## 🐞 **Did you find a bug?**

### Please follow these steps before opening an issue:

### ✔ **1. Check if the bug was already reported**

Search existing issues:
👉 [Old Issues](https://github.com/maybe-adev/pearlen/issues)

### ✔ **2. If not found, open a new Issue**

Use this link:
👉 [Create New Issue](https://github.com/maybe-adev/pearlen/issues/new)

A good bug report includes:

* Clear title
* Description of the issue
* Steps to reproduce
* Expected behavior
* Actual behavior
* Error logs (full, not cropped)
* Code sample or `.pearl` file causing the issue
* OS, Python version
  
---

## 🛠 **Did you write a patch that fixes a bug?**

### Steps:

1. Fork the repo
2. Create a branch:

   ```
   git checkout -b fix/my-bug
   ```
3. Commit your fix with a clear message:

   ```
   fix(parser): handle nested parentheses
   ```
4. Open a Pull Request:
   👉 [Pull Requests](https://github.com/maybe-adev/pearlen/pulls)

### Your PR description must include:

* What bug it fixes
* Why it happened
* How the fix works
* Before/after behavior
* Linked issue number

---

## ✨ **Did you fix whitespace or make a cosmetic change?**

Cosmetic-only PRs (formatting, unused imports, renaming files, minor refactors)
**may not be accepted** unless they improve stability, clarity, or maintainability.

---

## 🚧 **Do you want to add a new feature or change existing behavior?**

### Please do NOT open a GitHub Issue immediately.

Instead:

1. Start a discussion here:
   👉 **`discussions/` tab on GitHub**

2. Propose your idea and gather feedback

3. After reaching agreement, you may open a formal issue

4. Then start implementing your feature

This helps keep the issue tracker focused on **bugs + accepted features**.

---

## 🧠 **Do you have questions about the source code?**

Ask in:

* GitHub Discussions

We are happy to help contributors understand the codebase.

---

## 📚 **Do you want to improve the documentation?**

Pearlen documentation lives in:

```
docs/
```

You can contribute by improving:

* The language guide
* Syntax reference
* Examples
* Error explanations
* Parser or interpreter diagrams
* Internal architecture docs

Documentation PRs are very welcome.



## 🧪 Testing Contributions

### Python tests:

```
pytest
```

Before submitting your PR:

✔ JSON AST must be valid
✔ Pearlen CLI must run
✔ Python interpreter must evaluate correctly
✔ REPL must not crash

---

## ❤️ Thank You for Helping Build Pearlen!

Pearlen is an open-source effort powered by contributors like you.
We appreciate every bug report, pull request, documentation fix, and idea.
