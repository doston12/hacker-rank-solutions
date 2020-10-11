# set intersection operation

_ = input()
group1 = set(map(int, input().split()))
_ = input()
group2 = set(map(int, input().split()))

print(len(group1.intersection(group2)))