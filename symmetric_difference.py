
n = int(input())
numbers_n = set(list(map(int, input().split())))

m = int(input())
numbers_m = set(list(map(int, input().split())))

result = list(numbers_n.difference(numbers_m)) + list(numbers_m.difference(numbers_n))

for i in sorted(result):
    print(i)
