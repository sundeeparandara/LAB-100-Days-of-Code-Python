def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal()==False:
    if wall_on_right() == True:
        if front_is_clear() == False:
            turn_left()
        else:
            move()
    else:
        turn_right()
        if front_is_clear() == True:
            move()
        
            