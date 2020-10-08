from collections import defaultdict

n, m = map(int, input().split(' '))
a = defaultdict(list)
b = []
for x in range(n):
    temp = input()
    a[temp].append(x + 1)

for x in range(m):
    b.append(input())

for x in range(m):
    if b[x] in a.keys():
        for i in a[b[x]]:
            print(i, end=' ')
        print()
    else:
        print(-1)





