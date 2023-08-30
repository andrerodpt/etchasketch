from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
screen.listen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def rotate_conter_clockwise():
    tim.left(10)
def rotate_clockwise():
    tim.right(10)
def clear_drawing():
    screen.reset()

screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=rotate_conter_clockwise)
screen.onkeypress(key='d', fun=rotate_clockwise)
screen.onkeypress(key='c', fun=clear_drawing)

screen.exitonclick()