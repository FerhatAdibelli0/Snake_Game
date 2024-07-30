import time
from food import Food
from turtle import Screen
from snake_class import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

screen.listen()
screen.tracer(0)

food = Food()
snake = Snake()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_going_on = True

while is_going_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        is_going_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1::1]:
        # if segment == snake.head:
        #     print("This is head")
        #     pass
        if snake.head.distance(segment) < 10:
            is_going_on = False
            score.game_over()


screen.exitonclick()
