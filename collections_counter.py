from collections import Counter

shoes_count = int(input())
shoes = list(map(int, input().split(' ')))
shoes_sizes = Counter(shoes)
orders = int(input())
money = 0

for i in range(orders):
    size, price = map(int, input().split(' '))
    if shoes_sizes.get(size) is not None and shoes_sizes.get(size) > 0:
        money += price
        shoes_sizes[size] -= 1

print(money)
