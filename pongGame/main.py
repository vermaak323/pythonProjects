from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard


my_screen=Screen()
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black") 
my_screen.title("PONG GAME")
my_screen.tracer(0)


r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball=Ball()
scoreboard=Scoreboard()


my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")





game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()


    #detect collision with upper and lower walls 
    if ball.ycor()>250 or ball.ycor()<-250:
        ball.y_bounce()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.x_bounce()
        scoreboard.r_point()

    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()
        scoreboard.l_point()
    
        

    #when r paddle misses the ball
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    # when l paddle misses the ball
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()
