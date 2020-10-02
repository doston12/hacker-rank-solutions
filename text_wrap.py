import textwrap

def wrap(string, max_width):
    ans = ''
    for i in range(0, len(string), max_width):
        ans =  ans + (string[i:i+max_width]) + '\n'
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


