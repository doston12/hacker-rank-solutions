# checking strict superset property

my_set = set(map(int, input().split()))
n = int(input())
answer = True
for i in range(n):
    temp_set = set(map(int, input().split()))
    if not temp_set.issubset(my_set) or len(set(my_set.difference(temp_set))) < 1:
        answer = False

print(answer)