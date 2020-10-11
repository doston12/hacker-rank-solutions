# check subset

n = int(input())
ans = []
for i in range(n):
    _ = input()
    set1 = set(map(int, input().split()))
    _ = input()
    set2 = set(map(int, input().split()))
    ans.append(True if set2.intersection(set1) == set1 else False)

for a in ans:
    print(a)
