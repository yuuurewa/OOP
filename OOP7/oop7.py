import tkinter as tk
from tkinter import ttk

def add_item_left():
    item = entry.get()
    if item:
        listbox_left.insert(tk.END, item)
        entry.delete(0, tk.END)

def add_item_right():
    item = entry.get()
    if item:
        listbox_right.insert(tk.END, item)
        entry.delete(0, tk.END)

def remove_item_left():
    try:
        index = listbox_left.curselection()[0]
        listbox_left.delete(index)
    except IndexError:
        print("Не выбран элемент")

def remove_item_right():
    try:
        index = listbox_right.curselection()[0]
        listbox_right.delete(index)
    except IndexError:
        print("Не выбран элемент")

def move_to_right():
    try:
        index = listbox_left.curselection()[0]
        item = listbox_left.get(index)
        listbox_left.delete(index)
        listbox_right.insert(tk.END, item)
    except IndexError:
        print("Не выбран элемент")

def move_to_left():
    try:
        index = listbox_right.curselection()[0]
        item = listbox_right.get(index)
        listbox_right.delete(index)
        listbox_left.insert(tk.END, item)
    except IndexError:
        print("Не выбран элемент")


root = tk.Tk()
root.title("Listbox")

entry = ttk.Entry(root)
entry.pack(pady=5)

add_left_button = ttk.Button(root, text="Добавить в левый", command=add_item_left)
add_left_button.pack(pady=2)

add_right_button = ttk.Button(root, text="Добавить в правый", command=add_item_right)
add_right_button.pack(pady=2)

listbox_left = tk.Listbox(root)
listbox_left.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

listbox_right = tk.Listbox(root)
listbox_right.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

remove_left_button = ttk.Button(root, text="Удалить из левого", command=remove_item_left)
remove_left_button.pack(pady=2)

remove_right_button = ttk.Button(root, text="Удалить из правого", command=remove_item_right)
remove_right_button.pack(pady=2)

move_right_button = ttk.Button(root, text=">>", command=move_to_right)
move_right_button.pack(pady=2)

move_left_button = ttk.Button(root, text="<<", command=move_to_left)
move_left_button.pack(pady=2)

root.mainloop()
