from turtle import *


#we want to paint a house

#step 1: draw a square
width(7)
speed(30)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(75)

color("brown")
begin_fill()
left(90)
forward(100)       #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()


color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(75, 135)
pendown()

right(60)
color("cyan")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(135, 150)
pendown()

begin_fill()
forward(15)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(25)
end_fill()


exitonclick()