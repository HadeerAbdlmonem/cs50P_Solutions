0# 🐍 CS50P — Introduction to Programming with Python (2024)

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50-Python-red?style=for-the-badge&logo=harvard&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> ✨ My personal collection of solutions for **Harvard's CS50's Introduction to Programming with Python (CS50P)**, organized week-by-week and refactored for clean style, clear naming, and helpful comments.

---

## 📖 About

This repository contains my solutions to the problem sets from **CS50P (2024)**, organized into one folder per course week — exactly how the course itself is structured. Each script tackles a small, self-contained challenge, growing in complexity as the weeks progress: from simple functions and conditionals, all the way to regular expressions and object-oriented programming.

Every file has been reviewed and polished to:

- ✅ Follow **PEP 8** style conventions
- ✅ Use **clear, descriptive variable and function names**
- ✅ Include a short **docstring** explaining what each program does
- ✅ Wrap logic in a `main()` function with an `if __name__ == "__main__":` guard
- ✅ Fix small bugs found in the original attempts (typos, edge cases, logic slips)

---

## 🗓️ Weekly Roadmap

| Week | 📁 Folder | 🎯 Topic | 🔑 Highlights |
|---|---|---|---|
| 0 | [`week0_functions_variables`](week0_functions_variables) | 🐣 Functions, Variables | Indoor Voice, Playback Speed, Making Faces, Einstein, Tip Calculator |
| 1 | [`week1_conditionals`](week1_conditionals) | 🤔 Conditionals | Deep Thought, File Extensions, Meal Time |
| 2 | [`week2_loops`](week2_loops) | 🔁 Loops | camelCase, Coke Machine, Twttr, Nutrition Facts |
| 3 | [`week3_exceptions`](week3_exceptions) | 🧯 Exceptions | Fuel Gauge, Felipe's Taqueria, Grocery List, Outdated |
| 4 | [`week4_libraries`](week4_libraries) | 📚 Libraries | Emojize, Figlet, Adieu, Guessing Game, Little Professor, Bitcoin |
| 5 | [`week5_unit_tests`](week5_unit_tests) | 🧪 Unit Tests | Back to the Bank, Re-requesting a Vanity Plate |
| 6 | [`week6_file_io`](week6_file_io) | 🗂️ File I/O | Lines of Code, Pizza Py, Scourgify, CS50 P-Shirt |
| 7 | [`week7_regular_expressions`](week7_regular_expressions) | 🔍 Regular Expressions | NUMB3RS, Watch on YouTube, Working 9 to 5, Um, Response Validation |
| 8 | [`week8_oop`](week8_oop) | 🧱 OOP | Cookie Jar, Seasons of Love |
| — | [`extra_projects`](extra_projects) | 🎨 Extras | Tkinter Calculator, Text-to-Speech app |

Each folder has its **own README** with a description of every script, how to run it, and the concepts it practices. 👀

---

## 🚀 Getting Started

### Prerequisites

- Python **3.11+**
- `pip` for installing dependencies

### Installation

```bash
git clone https://github.com/<your-username>/cs50p-2024.git
cd cs50p-2024
pip install -r requirements.txt
```

### Running a script

```bash
cd week0_functions_variables
python indoor.py
```

### Running the tests

```bash
pip install pytest
cd week5_unit_tests
pytest
```

---

## 📦 Dependencies

Some scripts rely on third-party packages:

```
requests
pyfiglet
emoji
tabulate
validators
inflect
pyttsx3
```

Install them all at once with:

```bash
pip install -r requirements.txt
```

---

## 🏗️ Repository Structure

```
cs50p_2024/
├── week0_functions_variables/
│   ├── README.md
│   └── ...
├── week1_conditionals/
│   ├── README.md
│   └── ...
├── week2_loops/
├── week3_exceptions/
├── week4_libraries/
├── week5_unit_tests/
├── week6_file_io/
├── week7_regular_expressions/
├── week8_oop/
├── extra_projects/
├── requirements.txt
└── README.md   ← you are here
```

---



## 👩‍💻 Author

**Hadeer**
Senior AI/ML ENGINEER for digital ic design and AI ACCELERATOR 

---

## 📄 License

This project is for educational purposes as part of Harvard's **CS50P** course. Feel free to explore, but please respect [CS50's Academic Honesty policy](https://cs50.harvard.edu/python/2022/honesty/) if you're taking the course yourself. 🎓
