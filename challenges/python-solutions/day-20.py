import re

sentence = input()
words = re.split(r'[!\[\],\?.\\_\'@\+\s]*', sentence)

words = [word for word in words if word != '']
print(len(words))
for word in words:
    print(word)
