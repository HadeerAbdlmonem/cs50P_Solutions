"""
Read grocery items from the user (one per line) until EOF, then print:
- every item entered, in order
- each distinct item, in order of first appearance
- how many times each distinct item was entered
"""

from collections import Counter


def main():
    items = []
    while True:
        try:
            item = input("Item: ").lower()
            items.append(item)
        except EOFError:
            break

    unique_items = list(dict.fromkeys(items))  # preserves first-seen order
    counts = Counter(items)

    print(items)
    print(unique_items)
    print([counts[item] for item in unique_items])


if __name__ == "__main__":
    main()
