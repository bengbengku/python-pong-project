from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_POSITION = (350, 0)
L_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game With Python")
screen.tracer(0)

r_paddle = Paddle(R_POSITION)
l_paddle = Paddle(L_POSITION)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Deteksi benturan dan pantulkan bola, untuk atas dinding
    if ball.ycor() > 280 or ball.ycor() < -280:
        """Kondisi untuk pantulan dinding"""
        ball.bounce_y()

    #deteksi benturan terhadap paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Deteksi ketika R paddle tidak mengenai bola
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Deteksi ketika R paddle tidak mengenai bola
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()