from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball = Ball()
score=Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  
    ball.move()
   
    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce 
        ball.bounce_y()
    #detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() >370 : 
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
