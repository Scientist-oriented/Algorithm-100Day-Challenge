# day2 4/4 Sunday

import sys
sys.stdin=open("input.txt", "r")

# 답코드
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
    # 방문한 위치를 표시하기 위해서 별도로 설정함
x, y , direction = map(int, input().split())

d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    # 일단 1을 빼고 예외는 아래에 처리하는 것이 더 일반적인 코딩방식이다
        # try else 방식을 활용한다.
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
# 이 변수를 이용해서 한바퀴 돌았는지를 체크함
    # 따라서 아래 반복문에서 일단 돌고 -> 예외사항체크의 순서로 코드를 진행할 수 있게 됨.

while True:
    turn_left()
    print("d: " + str(direction))

    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0  and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        print(x, y)
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            # 바다여부를 확인할 필요가 없는 이유는 뒤에서 왔기 때문에
            x = nx
            y = ny
            print(x, y)
        else:
            print("No")
            break
        turn_time = 0

print(count)
# count는 방문한 곳의 갯수였음!
    # 다른 test case가 주어졌다면 문제 틀렸을 것....
    # 문제를 꼼꼼하게 읽고 정리해야 한다!!!



'''
# 이취코 p.118
# 내 코드
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
    # 일단 어떻게 하는 줄은 알겠는데 뭔가 구현실력이 부족한 느낌... 대략 1시간 정도 걸린 것 같다.
    # 중간중간에 자잘한 실수들이 많았다. 종이에 충분히 계획을 짜고 코딩을 할 것!
    # 방문한 칸수를 출력해야 함!!!!!


# 이취코 p.115
# 답코드

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
    # a, b, c ~ 순서대로 나올 때는 아스키코드를 활용하면 좋다

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 내코드

position = input()

x = int(position[1])
yCases = ['a', 'b', 'c', 'd', "e", 'f', 'g', "h"]
y = int(yCases.index(position[0]) + 1)

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -1, -2]
    
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)


# 이취코 p. 133

# 정답코드
    # 훨씬 단순하게 풀 수 있었음
    # 파이썬은 문자열을 그대로 활용하면 되었음

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 내 코드
n = int(input())

time = [0, 0, 0, 0]

def changeSecondToTime(n):
    hour = str(100 + n // 3600)
    n = n % 3600
    minute = str(100 + n // 60)
    n = n % 60
    second = str(100 + n)
    time = [hour[1], hour[2], minute[1], minute[2], second[1], second[2]]
    return time

print(changeSecondToTime(3600))

result = 0

for second in range((n + 1) * 3600):
    # 처음에 그냥 n만 곱해서 틀렸음 -> 00:00:00 ~ n:59:59는 n + 1 시간이다!
    time = changeSecondToTime(second)
    if '3' in time:
        result += 1

print(result)
'''