import sys
sys.stdin=open("input.txt", "r")



"""


# 이것이 취업을 위한 코딩테스트 p.110

# 정답코드
n = int(input())
x, y = 1, 1
    # 굳이 좌표를 리스트로 묶을 필요는 없다. (나중에 출력할 때 번거로움)

plans = input().split()

# L, R, U, D에 따른 이동방향
    # 좌표와 관련된 전후좌후 문제를 풀 때 활용

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']
    # 명령어와 이동좌표의 index를 일치시켜 놓는다.

for plan in plans:
    for i in rnage(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
    x, y = nx, ny

print(x, y)

# 내 코드
n = int(input())

position = [1, 1]
# 처음에 가로, 세로인줄 알았는데 반대였음 -> 문제 잘 읽기!
commands = list(input().split())

for command in commands:
    if command == 'L':
        if position[1] <= 1:
            continue
        else:
            position[1] -= 1
    if command == 'R':
        if position[1] >= n:
            continue
        else:
            position[1] += 1
    if command == 'U':
        if position[0] <= 1:
            continue
        else:
            position[0] -= 1
    if command == 'D':
        if position[0] >= n:
            continue
        else:
            position[0] += 1

print(position[0], position[1])

"""
