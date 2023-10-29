from turtle import Turtle

ALIGN = "center"

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		with open("./data.txt", 'r') as fd:
			self.highscore = int(fd.read())
		self.color("white")
		self.penup()
		self.goto(0, 260)
		self.hideturtle()
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def reset(self):
		if self.score > self.highscore:
			self.highscore = self.score
			with open("./data.txt", 'w') as fd:
				fd.write(f"{self.highscore}")
		self.score = 0

