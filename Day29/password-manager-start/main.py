from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json


def gen_pass():
    password_entry.delete(0, END)
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',',
               '.',
               '?', '/']

    num_alpha = random.randint(8, 15)
    num_numbers = random.randint(2, 4)
    num_symb = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(alphabets) for i in range(num_alpha)]
    password_list += [random.choice(numbers) for j in range(num_numbers)]
    password_list += [random.choice(symbols) for k in range(num_symb)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_feature():
    email_entered = email_entry.get()
    password_entered = password_entry.get()
    website_entered = website_entry.get()
    new_data = {website_entered:
        {
            "email": email_entered,
            "password": password_entered,
        }
    }
    if email_entered == "" or password_entered == "" or website_entered == "":
        messagebox.showinfo(message="You left one or more field empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            email_entry.delete(0, END)


def search():
    to_search = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found")
    else:
        try:
            email_needed = data[to_search]["email"]
            pass_needed = data[to_search]["password"]
        except KeyError:
            messagebox.showinfo(title="Warning", message=f"No records found for website: {to_search}")
        else:
            messagebox.showinfo(title="email/password", message=f"Email: {email_needed}\nPassword: {pass_needed}")
            pyperclip.copy(pass_needed)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=220)
img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")

email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

email_entry = Entry(width=35)
email_entry.insert(0, "vishwajeet@xyz.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate password", width=14, command=gen_pass)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=add_feature)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
