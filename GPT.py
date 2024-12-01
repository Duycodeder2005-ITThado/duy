from turtle import *
from math import sin,cos,radians

setup (650,650)
bgcolor('#10A37F')
step = 360/6
x = cos(radians(42))*150
y = sin(radians(42))*150
up()
goto(x,y)
seth(42-60)
fd(150)
lt(90)
down()
color('white')
begin_fill()
for i in range(6):
    circle(150, 120)
    rt(60)
end_fill()

color('#10A37F')
a = 90
up()
begin_fill()
for i in range(7):
    x = cos(radians(a))*75
    y = sin(radians(a))*75
    goto(x, y)
    down()
    a+=step
end_fill()

a = 0
for i in range(6):
    up()
    goto(0, 0)
    seth(a)
    lt(132.9)
    fd(95.5)
    down()
    begin_fill()
    rt(42.9)
    fd(58)
    rt(59)
    fd(137.7)
    rt(0)
    circle(-113.9, 130.3)
    rt(110.4)
    fd(139.3)
    rt(5.7)
    circle(22.1, 66)
    rt(0.6)
    fd(166.2)
    end_fill()
    a+=60

hideturtle()
done()
