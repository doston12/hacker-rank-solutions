# collections deque - memory and access efficient datastructure, retrieve data from both ends
#   at O(1)

from collections import deque

n = int(input())
deq = deque()

for i in range(n):
    x = input()
    if x.find(' ') > 0:
        method_name, number = x.split()
        if method_name == 'append':
            deq.append(int(number))
        elif method_name == 'appendleft':
            deq.appendleft(int(number))
    else:
        if x == 'pop':
            deq.pop()
        elif x == 'popleft':
            deq.popleft()

for x in deq:
    print(x, end=' ')
