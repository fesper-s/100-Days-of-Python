sentence = input()

list_of_words = sentence.split()

result = {words:len(words) for words in list_of_words}

print(result)
