# set mutations

_ = input()
my_set = set(map(int, input().split()))

m = int(input())
for i in range(m):
    method_name, x = input().split()
    new_set = set(map(int, input().split()))
    if method_name == 'intersection_update':
        my_set.intersection_update(new_set)
    elif method_name == 'update':
        my_set.update(new_set)
    elif method_name == 'symmetric_difference_update':
        my_set.symmetric_difference_update(new_set)
    elif method_name == 'difference_update':
        my_set.difference_update(new_set)

print(sum(my_set))
