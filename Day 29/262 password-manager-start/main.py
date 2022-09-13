import random
import tkinter
from tkinter import messagebox
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_generate_list_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_generate_list_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_generate_list_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_generate_list = password_generate_list_letters + password_generate_list_symbols + password_generate_list_numbers

    random.shuffle(password_generate_list)
    password_generate_result = ''.join(password_generate_list)
    input_password.insert(0, password_generate_result)

    pyperclip.copy(password_generate_result)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global input_website
    global input_user
    global input_password

    website = input_website.get()
    user = input_user.get()
    password = input_password.get()

    # messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {user} \nPassword: "
    #                                            f"{password} \nIs it ok to save?")
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        with open("data.txt", mode="a") as file_data:
            line = f"{website} | {user} | {password}\n"
            input_website.delete(0, tkinter.END)
            input_password.delete(0, tkinter.END)
            # input_user.delete(0, tkinter.END)
            file_data.write(line)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
mypass_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0)

# Label
label_website = tkinter.Label(text="Website", font=(FONT_NAME, 10, "bold"))
label_website.grid(column=0, row=1)

label_user = tkinter.Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
label_user.grid(column=0, row=2)

label_password = tkinter.Label(text="Password:", font=(FONT_NAME, 10, "bold"))
label_password.grid(column=0, row=3)

# Entry
input_website = tkinter.Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_user = tkinter.Entry(width=35)
input_user.grid(column=1, row=2, columnspan=2)
input_user.insert(0, "huyleezoan@gmail.com")

input_password = tkinter.Entry(width=21)
input_password.grid(column=1, row=3)

# Button

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_buton = tkinter.Button(text="Add", width=36, command=save)
add_buton.grid(column=1, row=4)
window.mainloop()
