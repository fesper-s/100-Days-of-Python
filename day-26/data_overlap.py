with open("file1.txt", "r") as fd:
    list1 = fd.readlines()
with open("file2.txt", "r") as fd2:
    list2 = fd2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)
