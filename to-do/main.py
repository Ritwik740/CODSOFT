import tkinter as tk
from tkinter import ttk

def create_label(text, font_size, parent, bg_color="black", fg_color="white",side="left",padx=100):
    label = ttk.Label(parent, text=text, font=("Arial", font_size), background=bg_color, foreground=fg_color)
    label.pack(side=side, padx=padx) 
    return label


def addNewToDo():
    def displayToDo():
        labelContent = entry.get()
        create_label(text=labelContent, font_size=12, parent=root,side="bottom")
        
        
        
    addNewToDoWindow = tk.Toplevel(root)
    addNewToDoWindow.title("Add New To-Do")

    entry_var = tk.StringVar()
    entry = ttk.Entry(addNewToDoWindow, textvariable=entry_var, width=50)
    submitToDo = tk.Button(addNewToDoWindow, text="Submit To-Do", command=displayToDo)
    
    entry.pack(pady=20)
    submitToDo.pack()

root = tk.Tk()
root.title("To-Do List")
# Set the window size to fit the screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Set the background color
root.configure(background="black", padx=30, pady=30)

# Title Label
title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 48), bg="black", fg="white")
title_label.pack(fill='x')

addToDoBtn = ttk.Button(root, text="Click to add a new To-Do", command=addNewToDo)
addToDoBtn.pack()

# Create Labels in the same line
todo_label = ttk.Label(root, text="To-Do", font=("Arial", 12), background="black", foreground="white")
todo_label.pack(side="left", padx=250)
deadline_label = create_label("Deadline", 12, root)
mark_completed_label = create_label("Mark as Completed", 12, root)
delete_todo_label = create_label("Delete To-Do", 12, root)

root.mainloop()
