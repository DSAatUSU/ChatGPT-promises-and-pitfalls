# This program will create a random populated text box
# run pip3 install requests
import random
import tkinter as tk
from tkinter import ttk
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content
WORDS = str(words, 'utf-8').splitlines()

root = tk.Tk()
root.title("Random Selectionbox")
root.geometry("600x400")

ttk.Label(root, text = "This box is filled with random items.",
          background = 'white', foreground = 'grey',
          font = ('Times New Roman', 15)).grid(row = 0, column = 1)

ttk.Label(root, text = "Select the item :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)

box = tk.StringVar()
item_chosen = ttk.Combobox(root, width = 30, textvariable=box)

item_list = []

n = random.randint(5, 10)

for i in range(n):
    item_list.append(WORDS[random.randrange(1000)])

item_tuple = tuple(item_list)

item_chosen['values'] = item_tuple

item_chosen.grid(column=1, row=5)
item_chosen.current()
root.mainloop()
