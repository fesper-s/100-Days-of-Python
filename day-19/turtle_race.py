from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
x = -230
y = -100
for i in range(6):
	turtles.append(Turtle(shape="turtle"))
	turtles[i].color(colors[i])
	turtles[i].penup()
	turtles[i].goto(x, y)
	y += 40

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in turtles:
		if turtle.xcor() > 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You've won! The {winning_color} turtle is the winner!")
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")
		rand_distance = randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()
