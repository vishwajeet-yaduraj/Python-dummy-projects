from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    global reps
    reps =0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    if reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tick_text = ""
        for _ in range(reps//2):
            tick_text += "✔"
            tick_label.config(text=tick_text)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(103, 88, image=tomato_pic)
timer_text = canvas.create_text(103, 115, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", fg="black", command=start_timer)
start_button.config(padx=5)
start_button.grid(row=2, column=0)

Reset_button = Button(text="Reset", fg="black", command=reset_timer)
Reset_button.config(padx=5)
Reset_button.grid(row=2, column=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()
