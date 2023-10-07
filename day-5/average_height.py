student_heights = input().split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

total_height = 0
for student_height in student_heights:
	total_height += student_height

average_height = total_height / len(student_heights)

print(f"total height = {total_height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(average_height)}")
