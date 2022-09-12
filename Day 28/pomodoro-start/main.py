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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time


# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

def count_down(count):
    # "00:00"
    count_min = count / 60
    canvas.itemconfig(tomato_time, text=count_min)

    if count > 0:
        window.after(1000, count_down, count - 1)


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

reset_button = tkinter.Button(text="Reset", background="white", highlightthickness=0)
reset_button.grid(row=2, column=2)

# Create check
check_mark = tkinter.Label(text="✓", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 15))
check_mark.grid(column=1, row=3)

window.mainloop()
