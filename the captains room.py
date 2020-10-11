# the captain's room

n = int(input())
rooms = input().split()
unique_rooms1 = set()
unique_rooms2 = set()

for x in rooms:
    if x not in unique_rooms1:
        unique_rooms1.add(x)
    else:
        unique_rooms2.add(x)

print(list(unique_rooms1.difference(unique_rooms2))[0])

