# combinations with replacements
from itertools import combinations_with_replacement

text, number = input().split()
text_chars = list(text)
text_chars.sort()

res = list(combinations_with_replacement(text_chars, int(number)))
for elem in res:
    temp = ''
    for x in elem:
        temp = temp + x
    print(temp)
