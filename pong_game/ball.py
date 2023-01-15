from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("light blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed(1.4)
    
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    
    def bounce(self):
        self.y_move *= -1
    
    def hit(self):
        self.x_move *= -1