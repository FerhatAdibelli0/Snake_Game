import random
from turtle import Turtle, Screen

# Create a turtle object
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("coral")
# my_turtle.backward(300)
# my_screen = Screen()

# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirrel", "Charmane"])
# table.add_column("Type", ["Electricity", "Water", "Fire"])
#
# print(table)

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     new_heading = tim.heading() + 90
#     tim.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 90
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
#
#
# print(tim.heading())
# screen.listen()
# screen.exitonclick()


from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will the rice? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.speed(3)
    tim.setposition(x=-230, y=y_position[index])
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_num = random.randint(0, 10)
        turtle.forward(random_num)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've win :-) ... {turtle.pencolor()} is winning color.")
            else:
                print(f"You've lost :-( ... {turtle.pencolor()} is winning color.")


screen.exitonclick()
