import tkinter as tk
from tkinter import messagebox

# Define what each button should do
def open_records():
    messagebox.showinfo("Navigation", "Opening: Manage Student Records")

def open_converter():
    messagebox.showinfo("Navigation", "Opening: Convert Numbers")

def open_binary():
    messagebox.showinfo("Navigation", "Opening: Binary & Float Representations")

def open_recursion():
    messagebox.showinfo("Navigation", "Opening: Recursion Functions")

def open_enhancements():
    messagebox.showinfo("Navigation", "Opening: Stack, Queue, Linked List")

# Main window
root = tk.Tk()
root.title("Digital Data Tool 🚀")
root.geometry("500x500")
root.resizable(False, False)

# Center frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Title
title = tk.Label(frame, text="Welcome to the Digital Data Tool 🚀", font=("Helvetica", 16, "bold"))
title.pack(pady=(0, 10))

# Subtitle
subtitle = tk.Label(frame, text="Select a section below to begin:", font=("Helvetica", 12))
subtitle.pack(pady=(0, 20))

# Buttons
btn_style = {"font": ("Helvetica", 11), "width": 40, "height": 2, "bd": 2, "relief": "groove"}

tk.Button(frame, text="📘 Manage student records", command=open_records, **btn_style).pack(pady=5)
tk.Button(frame, text="🔢 Convert numbers to binary, octal, and hex", command=open_converter, **btn_style).pack(pady=5)
tk.Button(frame, text="🧠 View binary & float representations", command=open_binary, **btn_style).pack(pady=5)
tk.Button(frame, text="🔁 Perform recursion: factorial & Fibonacci", command=open_recursion, **btn_style).pack(pady=5)
tk.Button(frame, text="⚙️ Stack, queue, and linked list features", command=open_enhancements, **btn_style).pack(pady=5)

root.mainloop()

#trial
