import sys
sys.stdin=open("input.txt", "r")

# 이취코 p.325 자물쇠와 열쇠

def solution(n, build_frame):
    field = [[-1] * (n + 1) for _ in range(n + 1)]
    
    for build in build_frame:
        x, y, a, b = build

        if a == 0: # 기둥일 때
            if b == 1: # 기둥 설치
                if a == 0 or field[a - 1][b] != -1 or field[a][b - 1] != -1:
                    field[a][b] = 0
                else:
                    continue
            else: # 기둥 삭제
                if field[a - 1][b] == -1:
                    field[a][b] = -1
                else:
                    continue
        else: # 보
            if b == 1: # 보 설치
                if a != 0 and (field[a - 1][b] != -1 or field[a][b - 1] != -1):
                    field[a][b] = 1
                else:
                    continue
            else: # 보 삭제
                if field[a][b + 1] == -1:
                    field[a][b] = -1
                else:
                    continue
    
    result = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != -1:
                result.append([i, j, field[i][j]])

    result.sort(key= lambda x: (x[0], x[1]))
    
    return result        


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(5, build_frame))