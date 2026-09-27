# 🗂️ Week 6 — File I/O

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-File%20I%2FO-9932CC?style=flat-square)

> Reading from and writing to files — the moment programs start interacting with the outside world. 💾

---

## 📂 Problems in this folder

| Script | Problem | 💡 Summary |
|---|---|---|
| `lines.py` | 📄 Lines of Code | Counts substantive lines of code in a `.py` file |
| `pizza.py` | 🍕 Pizza Py | Pretty-prints a pizza menu CSV as a table (uses `regular.csv`) |
| `scourgify.py` | 🧹 Scourgify | Cleans up a names CSV (`before.csv` → `after.csv` format) |
| `shirt.py` | 👕 CS50 P-Shirt | File-handling scaffold for an image-overlay exercise |

## 📊 Data files

| File | Used by | Description |
|---|---|---|
| `regular.csv` | `pizza.py` | A sample pizza menu (sizes & toppings) |
| `before.csv` | `scourgify.py` | Sample "Last, First" names + house, before cleanup |
| `after.csv` | `scourgify.py` | The expected "First, Last, House" output format |

---

## ▶️ How to run

```bash
python lines.py lines.py
python pizza.py regular.csv
python scourgify.py before.csv cleaned.csv
python shirt.py input.jpg output.jpg
```

## 🧠 Concepts practiced

- Opening files with `with open(...) as file:`
- Reading and writing CSV files with the `csv` module
- Command-line arguments (`sys.argv`)

---

⬅️ [Back to main README](../README.md)
