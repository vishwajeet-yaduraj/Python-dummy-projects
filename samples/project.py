from tkinter import *


def clicked():
    a = float(inp.get())
    a *= 1.6
    zero_label.config(text=f"{round(a,2)}")


window = Tk()
window.title("Miles to Km converter")
window.minsize(height=300, width=500)
window.config(padx=150, pady=30)

# Labels

miles_label = Label(text="Miles", font=("Comic Sans MS", 10, "bold"))
miles_label.config(padx=20)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to", font=("Comic Sans MS", 10, "bold"))
is_equal_label.config(padx=10)
is_equal_label.grid(row=1, column=0)

zero_label = Label(text="0", font=("Times New Roman", 15, "normal"))
zero_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Comic Sans MS", 10, "bold"))
km_label.config(padx=10)
km_label.grid(row=1, column=2)

# Entry

inp = Entry(width=7)  # Thala for a reason
inp.grid(row=0, column=1)

# Button

button = Button(text="Calculate", command=clicked)
button.grid(row=3, column=1)

window.mainloop()
