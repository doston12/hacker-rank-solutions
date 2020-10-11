# set discard remove and pop methods

n = int(input())
numbers = set(map(int, input().split()))

m = int(input())
for i in range(m):
    x = input()
    if x.find(' ') > 0:
        method_name, number = x.split()
        if method_name == 'remove':
            try:
                numbers.remove(int(number))
            except KeyError as e:
                print(e)
        elif method_name == 'discard':
            numbers.discard(int(number))
    else:
        if x == 'pop':
            try:
                numbers.pop()
            except KeyError as e:
                print(e)

print(sum(numbers))
