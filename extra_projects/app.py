"""A simple Tkinter calculator that adds, subtracts, multiplies, and divides two numbers."""

from tkinter import Tk, Label, Entry, Button, X

root = Tk()
root.title("Hadeer's Calculator")
root.geometry("500x500")

title_label = Label(
    root,
    text="This is a calculator",
    font=("Times New Roman", 20, "italic"),
    bg="black",
    fg="white",
)
title_label.pack(fill=X)

author_label = Label(root, text="Shimaa", bg="pink", fg="black")
author_label.pack()

first_number_label = Label(root, text="First number:", bg="green", fg="black")
first_number_label.pack()
first_number_entry = Entry(root)
first_number_entry.pack()

second_number_label = Label(root, text="Second number:", bg="green", fg="black")
second_number_label.pack()
second_number_entry = Entry(root)
second_number_entry.pack()


def show_result(symbol, operation):
    """Compute `operation` on the two entered numbers and display the result."""
    n1 = float(first_number_entry.get())
    n2 = float(second_number_entry.get())
    result = operation(n1, n2)
    result_label = Label(
        root,
        text=f"{n1} {symbol} {n2} = {result}",
        font=("Times New Roman", 20, "italic"),
        bg="black",
        fg="white",
    )
    result_label.pack()


add_button = Button(
    root,
    text="Show num1 + num2",
    font=("Arial", 10, "italic"),
    command=lambda: show_result("+", lambda a, b: a + b),
)
add_button.pack()

subtract_button = Button(
    root,
    text="Show num1 - num2",
    font=("Arial", 10, "italic"),
    command=lambda: show_result("-", lambda a, b: a - b),
)
subtract_button.pack()

multiply_button = Button(
    root,
    text="Show num1 x num2",
    font=("Arial", 10, "italic"),
    command=lambda: show_result("*", lambda a, b: a * b),
)
multiply_button.pack()

divide_button = Button(
    root,
    text="Show num1 / num2",
    font=("Arial", 10, "italic"),
    command=lambda: show_result("/", lambda a, b: a / b),
)
divide_button.pack()

root.mainloop()
