from turtle import Turtle, Screen
import pandas
image = "blank_states_img.gif"
screen = Screen()
screen.title('U.S States Game')
screen.addshape(image)
screen_t = Turtle()
screen_t.shape(image)

states_and_data = pandas.read_csv('50_states.csv')
states_name_list = states_and_data.state.to_list()
users_state = (screen.textinput(title='Guess the State', prompt="What's another state's name")).title()

if users_state in states_name_list:
    data_for_users_state = states_and_data[states_and_data.state == users_state]
    x_user_state = int(data_for_users_state.x)
    y_user_state = int(data_for_users_state.y)

    state = Turtle()
    state.pu()
    state.shape('circle')
    state.shapesize(0.1, 0.1)
    state.goto(x_user_state, y_user_state)
    state.write(users_state)


screen.exitonclick()
