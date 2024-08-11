from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
a_word = {}
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    data_dictionary = df.to_dict(orient="records")
else:
    data_dictionary = df.to_dict(orient="records")


def new_word():
    global a_word
    window.after_cancel(flip_timer)
    a_word = random.choice(data_dictionary)
    canvas.itemconfig(Title, text="French", fill="black")
    canvas.itemconfig(word, text=a_word["French"], fill="black")
    canvas.itemconfig(bg_img, image=front_img)
    window.after(3000, flip)


def flip():
    global a_word
    canvas.itemconfig(Title, text='English', fill="white")
    print(a_word)
    canvas.itemconfig(word, text=a_word["English"], fill="white")
    canvas.itemconfig(bg_img, image=back_img)


def is_known():
    data_dictionary.remove(a_word)
    data = pd.DataFrame(data_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()



window = Tk()
window.title("The Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")

back_img = PhotoImage(file="./images/card_back.png")
bg_img = canvas.create_image(400, 263, image=front_img)
Title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 260, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief="ridge", command=new_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
Right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
Right_button.grid(row=1, column=1)

new_word()
window.mainloop()
