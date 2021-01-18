def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while at_goal() == False:
    if wall_on_right() == True:
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()