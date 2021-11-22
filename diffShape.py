from turtle import Screen, Turtle
import random

colos = ["navy", "green", "gold", "dark orange", "red", "indigo", "coral", "dark slate blue", "lime", "teal", "gray", "dodger blue", "spring green", "firebrick", "tomato"]
t = Turtle()
t.penup()
t.setx(-100)
t.sety(-200)
t.pendown()
for i in range(3, 13):
    t.color(random.choice(colos))
    t.pensize(3)
    for j in range(i):
        angle = 360 / i
        t.forward(100)
        t.left(angle)

s = Screen()
s.exitonclick()