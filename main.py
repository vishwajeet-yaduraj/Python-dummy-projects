from tkinter import *


def clicked():
    my_label["text"] = inp.get()


window = Tk()
window.title("A GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label

my_label = Label(text="This is a Label", font=("Comic Sans MS", 14, "bold"))
my_label.grid(column=0, row=0)

# button
new_button = Button(text="NewButton")
# button.place(x=10, y=12)  # when we need precision
new_button.grid(column=2, row=0)

button = Button(text="click me", command=clicked)
# button.place(x=10, y=12)  # when we need precision
button.grid(column=1, row=1)

# Entry

inp = Entry(width=10)
inp.insert(END, string="Write")
inp.grid(column=3, row=2)

window.mainloop()
