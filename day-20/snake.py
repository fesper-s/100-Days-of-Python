from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		x = 0
		for i in range(3):
			self.segments.append(Turtle("square"))
			self.segments[i].color("white")
			self.segments[i].penup()
			self.segments[i].goto(x, 0)
			x -= 20

	def move(self):
		for seg_num in range(len(self.segments) - 1, 0, -1):
			x = self.segments[seg_num - 1].xcor()
			y = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(x, y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

