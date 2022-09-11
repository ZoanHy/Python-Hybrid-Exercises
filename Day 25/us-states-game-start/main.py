import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data_50_states = pandas.read_csv("50_states.csv")
all_states = data_50_states.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state's "
                                                                                           "name?").title()

    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    #
    # turtle.onscreenclick(get_mouse_click_coor)
    #
    # turtle.mainloop()
    # screen.exitonclick()

    # if answer_state:
    #     answer_state_temp = []
    #     for text in answer_state.lower().split(" "):
    #         answer_state_temp.append(text.capitalize())
    #     row = data_50_states[data_50_states.state == " ".join(answer_state_temp)]
    #     if pandas.notna(row.state).bool():
    #         x_cor = int(row.x)
    #         y_cor = int(row.y)
    #         new_state = turtle.Turtle()
    #         new_state.hideturtle()
    #         new_state.penup()
    #         new_state.goto(x_cor, y_cor)
    #         new_state.write(row.state.values[0])

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in guess_states:
            guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_50_states[data_50_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        print(guess_states)

# turtle.mainloop()

# states_to_learn.csv
