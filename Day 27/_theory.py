# Tkinter

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=560)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 18, "bold"))
# my_label.pack(expand=True)  # put label on screen and center
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text config")


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Click!!!")
    print(input.get())


my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack(side="top")

# Entry
input = tkinter.Entry(width=50)
input.pack()

# Text
text = tkinter.Text(height=5, width=35)
# Put cursor in textbox
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    # get the current value in spinbox
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check button
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkedbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkedbutton.pack()


# Radio button
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List box
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

# Unlimited Arguments

# def add(*args):
#     for n in args:
#         print(n)
#
#
# add(1, 3, 5, 6, 7)
