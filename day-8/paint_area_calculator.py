from math import ceil

def paint_calc(height, width, cover):
	num_cans = ceil(height * width / cover)
	print(f"You'll need {num_cans} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)