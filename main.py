import turtle
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title('U.S States Game')

screen.addshape(image)

turtle.shape(image)
screen.textinput(title='Guess the State', prompt="What's another state's name")


screen.exitonclick()
