target = int(input("Enter a number between 0 and 1000: "))

sum_even_num = 0
for i in range(2, target + 1, 2):
	sum_even_num += i

print(sum_even_num)