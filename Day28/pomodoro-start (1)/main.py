from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(height=200, width=224, bg = YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(103, 88, image=tomato_pic)
canvas.create_text(103, 115, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", fg="black")
start_button.config(padx=5)
start_button.grid(row=2, column=0)

Reset_button = Button(text="Reset", fg="black")
Reset_button.config(padx=5)
Reset_button.grid(row=2, column=2)

tick_text = "✔"
tick_label = Label(text=tick_text, fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)


window.mainloop()
