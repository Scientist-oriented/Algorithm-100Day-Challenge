import sys
sys.stdin=open("input.txt", "r")

# 이것이 취업을 위한 코딩테스트 p.110

n = int(input())

position = [1, 1]
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
