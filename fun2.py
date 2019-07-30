import turtle
turtle.goto(0,0)
turtle.tracer(1,0)

turtle.direction= None 

def up():
    turtle.direction = "Up"
    print('you pressed the up key.')
    on_move()

def down():
    turtle.direction='Down'
    print('you pressed the down button')
    on_move()

def left():
    turtle.direction='Left'
    print('you pressed the left button')
    on_move()
def right():
    turtle.direction='Right'
    print('you pressed the right button')
    on_move()
    
pixel_move=20

def on_move():
    turtle.position()
    x_pos=turtle.xcor()
    y_pos=turtle.ycor()
    if turtle.direction=='Up':
        turtle.goto(x_pos,y_pos+pixel_move)
        turtle.seth(90)
    elif turtle.direction=='Left':
        turtle.goto(x_pos-pixel_move,y_pos)
        turtle.seth(180)
    elif turtle.direction=='Right':
        turtle.goto(x_pos+pixel_move,y_pos)
        turtle.seth(0)
    else:
        turtle.goto(x_pos,y_pos-pixel_move)
        turtle.seth(270)
            
    

turtle.onkey(up, "Up")
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
##turtle.goto(0,0)
turtle.listen()



turtle.mainloop()
