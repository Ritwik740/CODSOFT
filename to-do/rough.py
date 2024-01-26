import tkinter as tk
from tkinter import ttk

def on_button_click():
    # Access the entered text from the entry widget
    entered_text = entry.get()
    print("Entered text:", entered_text)

root = tk.Tk()
root.geometry("400x200")
root.title("Themed Entry Example")

# Create a StringVar to store the text entered in the entry widget
entry_var = tk.StringVar()

# Create a ttk.Entry widget
entry = ttk.Entry(root, textvariable=entry_var, width=30)

# Pack the entry widget
entry.pack(pady=10)

# Create a button to demonstrate getting the entered text
button = ttk.Button(root, text="Get Entered Text", command=on_button_click)
button.pack()

root.mainloop()
