# itertools_permutations
from itertools import permutations

text, number = input().split(' ')
number = int(number)

characters = list(text)
characters.sort()

res = list(permutations(characters, number))
for elem in res:
    temp = ''
    for x in elem:
        temp = temp + str(x)
    print(temp)

