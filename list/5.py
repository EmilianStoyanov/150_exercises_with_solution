def match_words(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1

    return count


print(match_words(['abc', 'xyz', 'aba', '1221']))
"""
където дължината на низа е 2 или повече и първият и последният символ са еднакви  


Write a Python program to count the number of strings where the string
length is 2 or more and the
first and last character are same from a given list of strings.

"""
