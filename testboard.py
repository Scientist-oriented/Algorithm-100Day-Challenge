import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
a, b, d = map(int, input().split())
mapArray = list()

for _ in range(n):
    horizontalArray = list(map(int, input().split()))
    mapArray.append(horizontalArray)

mapArray[a][b] = 2


def rotate_left():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1


move_types = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

count = 0

while True:
    if count == 10:
        break
    if mapArray[a - 1][b] > 0 and mapArray[a + 1][b] > 0 and mapArray[a][b - 1] > 0 and mapArray[a][b + 1] > 0:
        next_a = a - move_types[d][0]
        next_b = b - move_types[d][1]

        if mapArray[next_a][next_b] == 1:
            break
        else:
            print("back")
            a = next_a
            b = next_b
            mapArray[a][b] = 2
            count += 1
    else:
        rotate_left()
        next_a = a + move_types[d][0]
        next_b = b + move_types[d][1]
        
        if mapArray[next_a][next_b] == 0:
            a = next_a
            b = next_b
            mapArray[a][b] = 2
            count += 1
            print("front")
        else:
            print("no move")
            continue

print(count)