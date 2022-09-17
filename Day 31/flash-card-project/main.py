# import
import random
import tkinter
from PIL import ImageTk, Image
import pandas

# Constant
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
data_array = {}
# Read data
try:
    with open("data/words_to_learn.csv") as file_data:
        data = pandas.read_csv(file_data)
except FileNotFoundError:
    with open("data/french_words.csv") as file_data:
        original_data = pandas.read_csv(file_data)
        data_array = original_data.to_dict(orient="records")
else:
    data_array = data.to_dict(orient="records")

# random
# def random_french_word():
# data_array = [{row.French: row.English} for (index, row) in data.iterrows()]

current_card = {}


def wrong_card():
    global current_card
    current_card = random.choice(data_array)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card['French'])


def right_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_array)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(main_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(main_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    data_array.remove(current_card)
    new_data = pandas.DataFrame(data_array)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    right_card()


# -------------------------------------- UI --------------------------------------

# image

# card_front = tkinter.PhotoImage(file="images/card_front.png")
# right = tkinter.PhotoImage(file="images/right.png")
# left = tkinter.PhotoImage(file="images/left.png")

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0, background=BACKGROUND_COLOR)
ImageTk.PhotoImage(Image.open("images/card_back.png"))
card_front = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card_back = ImageTk.PhotoImage(Image.open("images/card_back.png"))

main_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=(FONT, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# button
wrong_image = ImageTk.PhotoImage(Image.open("images/wrong.png"))
right_image = ImageTk.PhotoImage(Image.open("images/right.png"))
button_wrong = tkinter.Button(image=wrong_image, highlightthickness=0, command=wrong_card)
button_right = tkinter.Button(image=right_image, highlightthickness=0, command=right_card)

button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)
right_card()

window.mainloop()
