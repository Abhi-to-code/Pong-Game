from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game by Abhiram")

padle_right = Paddle()
padle_right.goto(350,0)

paddle_left = Paddle()
paddle_left.goto(-350,0)

ball = Ball()
game_stats = Score()
score_left = Score()
score_left.write_score_left()
score_right = Score()
score_right.write_score_right()

screen.listen()
screen.onkey(padle_right.move_up, "o")
screen.onkey(padle_right.move_down, "l")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (padle_right.distance(ball) < 50 and ball.xcor() > 320):
        ball.hit()
        score_right.increse_score_right()
        
    if (paddle_left.distance(ball) < 50 and ball.xcor() < -320):
        ball.hit()
        score_left.increase_score_left()

    if ball.xcor() > 400 or ball.xcor() < -400:
        game_stats.game_over()
        game_is_on = False

screen.exitonclick()