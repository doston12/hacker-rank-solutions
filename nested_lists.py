
students = []

def second_lowest_grade(students):
    grades = []
    for student in students:
        grades.append(student[1])

    temp_set = set(grades)
    return sorted(temp_set)[1]

def get_students(students, grade):
    ans = []
    for student in students:
        if student[1] == grade:
            ans.append(student[0])

    print_students(sorted(ans))

def print_students(students):
    for student in students:
        print(student)

for _ in range(int(input())):
    name = input()
    score = float(input())
    student = (name, score)
    students.append(student)


grade = second_lowest_grade(students)
get_students(students, grade)



