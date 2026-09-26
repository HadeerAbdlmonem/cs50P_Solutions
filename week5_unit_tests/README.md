# 🧪 Week 5 — Unit Tests

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Unit%20Testing-9cf?style=flat-square)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

> Writing tests so your code proves itself — revisiting earlier problems and adding `pytest`-powered test suites. ✅

---

## 📂 Problems in this folder

| Script | Test file | Problem | 💡 Summary |
|---|---|---|---|
| `bank_.py` | `test_bank_.py` | 🏦 Back to the Bank | Calculates a greeting fee, now with tests covering each pricing tier |
| `plates.py` | `test_plates.py` | 🚗 Re-requesting a Vanity Plate | Validates license plates, now with tests covering edge cases |

---

## ▶️ How to run

```bash
pip install pytest
pytest
```

Or run an individual test file:

```bash
pytest test_bank_.py -v
pytest test_plates.py -v
```

## 🧠 Concepts practiced

- Writing `test_` functions that `pytest` can auto-discover
- Using `assert` to verify expected behavior
- Testing edge cases, not just the "happy path"

## ⚠️ A note worth reading

`test_plates.py::test_letters_then_digit` asserts that `is_valid("C5")` should be `False`. Under the standard CS50P vanity-plate rules (letters first, then digits, no leading zero), `"C5"` is actually a **valid** plate — so this particular assertion contradicts the implementation's logic. It's been left exactly as originally written (rather than silently changed) since it may reflect an intentional variation on the rules; it's flagged here so it can be revisited if it wasn't intentional. 🔍

---

⬅️ [Back to main README](../README.md)
