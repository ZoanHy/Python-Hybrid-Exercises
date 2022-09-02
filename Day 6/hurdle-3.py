def turn_right():
    turn_left()
    turn_left()
    turn_left()

def run():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def move_forward():
    while front_is_clear() and not at_goal():
        move()
while not wall_in_front():
    move_forward()
while wall_in_front():
    run()
    while not at_goal() and not wall_in_front():
        move_forward()

    
