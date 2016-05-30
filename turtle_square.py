import turtle

def draw_square(some_turtle):
	for i in range(0,4):
		some_turtle.right(90)
		some_turtle.forward(100)

def draw_triangle(some_turtle):
	for i in range(0,3):
		some_turtle.right(120)
		some_turtle.forward(100)

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor('black')

	brad = turtle.Turtle()
	brad.color('red')
	brad.speed('fastest')
	brad.shape('turtle')

	draw_square(brad)
	draw_triangle(brad)

	window.exitonclick()

draw_shapes()