import turtle

def draw_triangle(some_turtle,length):
	some_turtle.right(60)
	some_turtle.begin_fill()
	for i in range(0,3):
		some_turtle.forward(length)
		some_turtle.right(120)
	some_turtle.end_fill()
	some_turtle.left(60)
	
def move_left(some_turtle,length):
	some_turtle.right(120)
	some_turtle.forward(length)
	some_turtle.left(120)

def move_right(some_turtle,length):
	some_turtle.forward(length)

def move_up(some_turtle,length):
	some_turtle.left(120)
	some_turtle.forward(length)
	some_turtle.right(120)

def recursive_draw(some_turtle, length, r):
	if r==0:
		draw_triangle(some_turtle,length)
	else:
		recursive_draw(some_turtle, length/2, r-1)
		move_left(some_turtle, length/2)
		recursive_draw(some_turtle, length/2, r-1)
		move_right(some_turtle, length/2)
		recursive_draw(some_turtle, length/2, r-1)
		move_up(some_turtle,length/2)

def draw_art():
	window = turtle.Screen()
	brad = turtle.Turtle()
	brad.goto(0,150)
	brad.clear()
	brad.shape('turtle')
	brad.speed('fastest')
	brad.color('green')
	recursive_draw(brad, 256, 3)
	window.exitonclick()

draw_art()
