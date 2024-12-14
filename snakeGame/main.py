from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
my_score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        my_score.increase_score()

    #detect collision with walls
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        
        game_is_on = False
        my_score.game_over()

    #detect collision with tail 
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            game_is_on=False
            my_score.game_over()    


screen.exitonclick()