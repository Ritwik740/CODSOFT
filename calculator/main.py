from tkinter import *

def process():
    try:
        number1 = int(E1.get())
        number2 = int(E2.get())
        operator = E3.get()

        if operator == "+":
            answer = number1 + number2
        elif operator == "-":
            answer = number1 - number2
        elif operator == "*":
            answer = number1 * number2
        elif operator == "/":
            answer = number1 / number2
        else:
            answer = "Invalid operator"

        E4.delete(0, END)  # Clear the previous answer
        E4.insert(0, answer)
        print(answer)

    except ValueError:
        E4.delete(0, END)
        E4.insert(0, "Invalid input")

top = Tk()
top.title("CALCULATOR")

# Set a maximum window size
top.maxsize(width=400, height=400)

top.geometry("400x400")

L1 = Label(top, text="CALCULATOR", font=("Segoe Print", 24), anchor="center")
L1.grid(row=0, column=1)

labels_text = ["Number 1", "Number 2", "Operator", "Answer"]
for i, text in enumerate(labels_text, start=1):
    label = Label(top, text=f"   \n {text} \n")
    label.grid(row=i, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)

E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)

E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)

E4 = Entry(top, bd=50)
E4.grid(row=4, column=1)

B = Button(top, text="SUBMIT FOR CALCULATION", command=process)
B.grid(row=5, column=1)

top.mainloop()
