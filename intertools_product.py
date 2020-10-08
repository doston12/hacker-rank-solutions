# itertools.product()


A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort()

result_list = []
for x in A:
    for y in B:
        result_list.append((x, y))

for x in result_list:
    print(x, end=' ')


