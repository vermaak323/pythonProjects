import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
for i in range(0,6):
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for cars in car_manager.all_cars:          
          if cars.distance(player)<20:
                game_is_on=False
                scoreboard.game_over()

    #detect successful crossing 
    if player.at_finish_line():
          player.goto_start()
          car_manager.levelup()
          scoreboard.increase_level()
          

screen.exitonclick()
    
    

