# Write a program to draw a face of a clock that looks something like this (you're going to see):

import turtle

window = turtle.Screen()
window.title("Exercise11.py")
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(3)
tess.shape("turtle")
tess.color("blue")

tess.stamp()
tess.penup()
for hour in range(12):
	tess.forward(120)
	tess.pendown()
	tess.forward(10)
	tess.penup()
	tess.forward(22)
	tess.stamp()
	tess.forward(-155)
	tess.right(30)

window.mainloop()
