import time
import turtle
from snake import Snake
from food import Food

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game: Fun to play")
screen.tracer(0.1)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #1s delay. 왜 이거 빼면 작동이 안하는지?
    snake.move()

    #Detect collision with food: distance(영역이내)
    if snake.head.distance(food) < 15:
        food.refresh()



screen.exitonclick()