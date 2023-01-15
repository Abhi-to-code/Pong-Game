from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.game_stats = Turtle()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.penup()
        self.color("grey")
    
    def write_score_right(self):
        self.goto(200,270)
        self.write(f"Score: {self.score_right}", align="center", font = ("Arail", 22,"normal"))
        self.hideturtle()
        
    def write_score_left(self):
        self.goto(-200,270)
        self.write(f"Score: {self.score_left}", align="center", font = ("Arail", 22,"normal"))

    def increse_score_right(self):
        self.score_right += 1
        self.clear()
        self.write(f"Score: {self.score_right}", align="center", font = ("Arail", 22,"normal"))

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.write(f"Score: {self.score_left}", align="center", font = ("Arail", 22,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font = ("Arail", 30,"normal"))
        if self.score_left > self.score_right:
            self.winner = "Left"
            self.goto(0,-100)
            self.write(f"The Winner is {self.winner}", align="center", font = ("Arail", 22,"normal"))

        elif self.score_left < self.score_right:
            self.winner = "Right"
            self.goto(0,-100)
            self.write(f"The Winner is {self.winner}", align="center", font = ("Arail", 22,"normal"))

        else:
            self.goto(0,-100)
            self.write(f"Draw Match!!!", align="center", font = ("Arail", 22,"normal"))
        
    