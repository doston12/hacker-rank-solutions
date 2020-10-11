# any or all solution

def check_palindrome_number(number):
    if int(str(number)[::-1]) == number:
        return True
    else:
        return False

def check_positiviness(number):
    if number > 0:
        return True
    else:
        return False

n = int(input())
numbers = list(map(int, input().split()))

if all([check_positiviness(x) for x in numbers]):
    if any([check_palindrome_number(x) for x in numbers]):
        print(True)
    else:
        print(False)
else:
    print(False)
