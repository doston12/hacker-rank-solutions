from collections import OrderedDict

n = int(input())
ordered_dict = OrderedDict()
for i in range(n):
    temp_str = input()
    index = temp_str.rfind(' ')
    a = temp_str[:index]
    b = int(temp_str[index:])
    if a in ordered_dict.keys():
        ordered_dict[a] = ordered_dict[a] + int(b)
    else:
        ordered_dict[a] = int(b)

for key, value in ordered_dict.items():
    print(key, value)
