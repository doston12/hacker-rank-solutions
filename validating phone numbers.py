# Validating phone numbers
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

n = int(input())
ans = []
pattern = '^[7-9]{1}\d{9}$'

for i in range(n):
    phone_number = input()
    match = re.search(pattern, phone_number)
    if match is not None:
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)
