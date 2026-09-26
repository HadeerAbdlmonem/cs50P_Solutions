"""A minimal Tkinter GUI that reads entered text aloud using pyttsx3."""

from tkinter import Tk, Label, Entry, Button
from pyttsx3 import init

root = Tk()
root.title("Text To Speech")
root.geometry("500x500")

prompt_label = Label(root, text="Text here:")
prompt_label.pack()

text_entry = Entry(root)
text_entry.pack()


def speak():
    engine = init()
    engine.say(text_entry.get())
    engine.runAndWait()


speak_button = Button(root, text="Text to speech", command=speak)
speak_button.pack()

root.mainloop()
