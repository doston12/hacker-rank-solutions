# example for using itertools combinations
from itertools import combinations

string, k = input().split()
k = int(k)
characters = list(string)
characters.sort()

for i in range(1, k+1):
    res = list(combinations(characters, i))
    for i in res:
        temp = ''
        for x in i:
            temp = temp + str(x)
        print(temp)