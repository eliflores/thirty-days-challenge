class Palindrome:
    def __init__(self):
        self.__stack = []
        self.__queue = []

    def pushCharacter(self, c):
        self.__stack.insert(0, c)

    def popCharacter(self):
        return self.__stack.pop(0)

    def enqueueCharacter(self, c):
        self.__queue.append(c)

    def dequeueCharacter(self):
        return self.__queue.pop(0)


# read the string s
W = input()
# Create the Palindrome class object
p = Palindrome()

l = len(W)
# push all the characters of string s to stack
for i in range(l):
    p.pushCharacter(W[i])
# enqueue all the characters of string s to queue
for i in range(l):
    p.enqueueCharacter(W[i])
f = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l):
    if p.popCharacter() != p.dequeueCharacter():
        f = False
        break
# finally print whether string s is palindrome or not.
if f:
    print("The word, " + W + ", is a palindrome.")
else:
    print("The word, " + W + ", is not a palindrome.")
