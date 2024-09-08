# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths,
# all angles the same):

#	• An equilateral triangle
#	• A square
#	• A hexagon (six sides)
#	• An octagon (eight sides)


import turtle

window = turtle.Screen()
window.title("Exercise5.py")
tess = turtle.Turtle()
tess.pensize(5)

tess.penup()
tess.backward(350)

# Equilateral triangle
tess.pendown()
for i in range(3):
	tess.forward(150)
	tess.left(120)
tess.penup()
tess.forward(200)

# Square
tess.pendown()
for i in range(4):
	tess.forward(130)
	tess.left(90)
tess.penup()
tess.forward(200)

# Hexagon
tess.pendown()
for i in range(6):
	tess.forward(75)
	tess.left(60)
tess.penup()
tess.forward(200)

# Octagon
tess.pendown()
for i in range(8):
	tess.forward(54)
	tess.left(45)

window.mainloop()
