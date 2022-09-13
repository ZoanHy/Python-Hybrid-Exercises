import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    text_timer.config(text="Timer")
    canvas.config(tomato_time="00:00")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = 10
    short_break_sec = 3
    long_break_sec = 5

    # text_timer.config(foreground=GREEN)
    # count_down(work_sec)
    if reps % 8 == 0:
        text_timer.config(foreground=RED, text="BREAK")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        text_timer.config(foreground=PINK, text="BREAK")
        count_down(short_break_sec)
    else:
        text_timer.config(foreground=GREEN, text="WORK")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time


# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

def count_down(count):
    # "00:00"
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(tomato_time, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            completed_task = int(reps / 2)
            global check_mark
            check_mark.config(text=''.join(["✓" for _ in range(1, (completed_task + 1))]))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, background=YELLOW)

# def say_something(thing):
#     print(thing)
#
#
# window.after(1000, say_something, "huy")

# Create text
text_timer = tkinter.Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 40, "bold"), background=YELLOW)
text_timer.grid(row=0, column=1)

# Create canvas
canvas = tkinter.Canvas(width=206, height=224, background=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
tomato_time = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
# count_down(5)

# Create button
start_button = tkinter.Button(text="Start", background="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", background="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Create check
check_mark = tkinter.Label(foreground=GREEN, background=YELLOW, font=(FONT_NAME, 15))
check_mark.grid(column=1, row=3)

window.mainloop()
