from turtle import Turtle, Screen

import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

#setting the screen
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating objects

snake = Snake()
food = Food()
score = ScoreBoard()

# keybinding

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

    

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.15)
    
    
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.new_food()
        snake.extend()
        score.new_score()
    
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        score.game_over()
        break

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()
            break





















screen.exitonclick()