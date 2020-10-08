# Enter your code here. Read input from STDIN. Print output to STDOUT
# collections.namedtuple()
from collections import namedtuple

number = int(input())
#CH1, CH2, CH3, CH4 = input().split('    ')
Students = namedtuple('Students', input().split())
sum_of_marks = 0
for i in range(number):
    w1, w2, w3, w4 = input().split()
    student = Students(w1, w2, w3, w4)
    sum_of_marks += float(student.MARKS)

print("%.2f" % (sum_of_marks / number))