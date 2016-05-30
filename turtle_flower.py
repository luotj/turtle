import turtle

def draw_diamond(some_turtle):
	for i in range(0,4):
		some_turtle.forward(80)
		some_turtle.right(60+(i%2)*60)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('white')

	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.speed('fastest')
	brad.color('red')

	for degree in range(0,360,5):
		draw_diamond(brad)
		brad.right(5)

	brad.right(90)
	brad.forward(240)
	window.exitonclick()

draw_art()