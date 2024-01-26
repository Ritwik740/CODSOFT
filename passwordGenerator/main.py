#importing modules
import random
import tkinter as tk
from tkinter import ttk


def password(length):
    # function to generate password of desired length
    myPassword = ""
    for _ in range(length):
        myPassword += chr(random.randint(33,126))
    return myPassword

root = tk.Tk()
root.title("RANDOM PASSWORD GENERATOR")     #setting title of window

# Set the background color
root.configure(background="black", padx=30, pady=30)

# Set the window size to fit the screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

def generatePassword():
    lengthOfPassword = entry.get()      #calling to get length of password
    entry.delete(0,"end")       #clearing entry box
    
    try :
        if int(lengthOfPassword) > 1:
            result_label.config(text=f"Your Password is: \n {password(int(lengthOfPassword))}")
        else:
            result_label.config(text="Please enter a number greater than 1.")
    except:
        result_label.config(text = "Enter a Valid Length")
        
        
title_label = tk.Label(root, text="RANDOM PASSWORD GENERATOR", font=("Segoe Script", 48), bg="black", fg="white")
title_label.pack(fill='x')

generatePasswordLabel = tk.Label(root, text="Enter Length of Password", font=("Arial", 36), bg="black", fg="white")
generatePasswordLabel.pack(fill='x')

entry_var = tk.IntVar()
entry = ttk.Entry(root, textvariable=entry_var, width=50)
submitToDo = tk.Button(root, text="Generate Password", command=generatePassword)
    
entry.pack(pady=20)
submitToDo.pack()

result_label = tk.Label(root, text="", font=("Arial", 24), bg="black", fg="white", wraplength=root.winfo_screenwidth() - 100)
result_label.pack(fill='x')



root.mainloop()

