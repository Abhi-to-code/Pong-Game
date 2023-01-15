from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_padle()

    def create_padle(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.color("light yellow")

    def move_up(self):
        self.sety(self.ycor() + 30)
        
    
    def move_down(self):
        self.sety(self.ycor() -30)
    