list_of_strings = input().split(',')

list_of_integers = [int(string) for string in list_of_strings]

result = [num for num in list_of_integers if num % 2 == 0]

print(result)
