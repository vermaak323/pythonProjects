from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self ) :
        super().__init__()
        self.score=0
        core=0
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)   
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}", align="center", font=('Arial', 24, 'normal'))

            
