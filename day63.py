import sys
sys.stdin=open("input.txt", "r")

# 사탕 게임
N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

def changeVertical(r, c):
    board[r][c], board[r + 1][c] = board[r][c], board[r + 1][c]

def changeHorizontal(r, c):
    board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

# groupBy로 해도 되고 이렇게 직접 index 하나하나 지나가면서 세도 됨!
def countCandy(line):
    ans = 0
    i = 0
    temp = 1
    while True:
        if i == len(line) - 1:
            ans = max(temp, ans)
            break

        if line[i] == line[i + 1]:
            temp += 1
        else:
            ans = max(temp, ans)
            temp = 1

        i += 1
    return ans

def getMaxCandy(r, c):
    maxCandy = 0
    for i in range(2):
        currentCandy = 

      