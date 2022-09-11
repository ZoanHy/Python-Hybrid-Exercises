from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


def mile_to_kilometers():
    mile = float(input_mile.get())
    kilometer = mile * 1.609
    kilometers_result_label.config(text=str(kilometer))


input_mile = Entry(width=20)
input_mile.grid(column=1, row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()
