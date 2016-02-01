def is_funny(word):
    word_length = len(word)
    j = word_length - 2
    for i in range(1, word_length):
        word_abs = abs(ord(word[i]) - ord(word[i - 1]))
        word_rev_abs = abs(ord(word[j]) - ord(word[j + 1]))
        if word_abs != word_rev_abs:
            return False
        j -= 1
    return True


number_of_test_cases = int(input())
for test_case in range(number_of_test_cases):
    if is_funny(input()):
        print('Funny')
    else:
        print('Not Funny')
