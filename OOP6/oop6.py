import turtle
import random
from threading import Thread

window = turtle.Screen()
def func(c, sh, sp):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.speed(sp)
    ball.shape(sh)
    ball.color(c)
    ball.up()
    randx = random.randint(-280, 280)
    randy = random.randint(-280, 280)
    ball.goto(randx, randy)
    ball.showturtle()
    dx = 3
    dy = 2

    while True:
        x, y = ball.position()
        if x + dx >= 300 or x + dx <= -300:
            dx = -dx
        if y + dy >= 300 or y + dy <= -300:
            dy = -dy
        ball.goto(x + dx, y + dy)

th1 = Thread(target=func, args=('violet', 'arrow', 0))
th2 = Thread(target=func, args=('green', 'turtle', 3))
th3 = Thread(target=func, args=('red', 'circle', 6))

th1.start()
th2.start()
th3.start()

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('black')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

turtle.mainloop()
