cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    f = [0, 1]
    for i in range(0, n-2):
        temp = f[i] + f[i+1]
        f.append(temp)
    return f
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))