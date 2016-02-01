class Palindrome:
    def __init__(self):
        self.__stack = []
        self.__queue = []

    def push_character(self, c):
        self.__stack.insert(0, c)

    def pop_character(self):
        return self.__stack.pop(0)

    def enqueue_character(self, c):
        self.__queue.append(c)

    def dequeue_character(self):
        return self.__queue.pop(0)


# read the string s
W = input()
# Create the Palindrome class object
p = Palindrome()

l = len(W)
# push all the characters of string s to stack
for i in range(l):
    p.push_character(W[i])
# enqueue all the characters of string s to queue
for i in range(l):
    p.enqueue_character(W[i])
f = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l):
    if p.pop_character() != p.dequeue_character():
        f = False
        break
# finally print whether string s is palindrome or not.
if f:
    print("The word, " + W + ", is a palindrome.")
else:
    print("The word, " + W + ", is not a palindrome.")
