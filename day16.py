# 이취코 p.329 기둥과 보 설치 답코드
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = list()
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
        
    answer = sorted(answer)
    return answer
'''
# 이취코 p.329 기둥과 보 설치 내코드 -> 테스트 케이스 외에는 통과 못함

def solution(n, build_frame):
    def isValid(x, y):
        if build[x][y] == 0:
            if y >= n:
                return False

            if y == 0:
                return True
            elif build[x][y - 1] == 0 or build[x - 1][y] == 1:
                return True
            else:
                return False
        elif build[x][y] == 1:
            if x >= n or y == 0:
                return False
                
            if build[x][y - 1] == 0 or build[x + 1][y - 1] == 0:
                return True
            elif build[x - 1][y] == 1 and build[x + 1][y] == 1:
                return True
            else:
                return False
        else:
            return True

    # 구조물 형태을 담는 이차원 리스트 (-1은 없고 0이 기둥, 1이 보)
    build = [[-1] * (n + 1) for _ in range(n + 1)]

    for frame in build_frame:
        x, y, t, cd = frame

        if cd == 1:
            if t == 0:
                build[x][y] = 0
                if isValid(x, y):
                    continue
                else:
                    build[x][y] = -1
            else:
                build[x][y] = 1
                if isValid(x, y):
                    continue
                else:
                    build[x][y] = -1
        else:
            if t == 0:
                build[x][y] = -1
                if (isValid(x, y + 1) and isValid(x - 1, y + 1)):
                    continue
                else:
                    build[x][y] = 0
            else:
                build[x][y] = -1
                if (isValid(x + 1, y) and isValid(x - 1, y)):
                    continue
                else:
                    build[x][y] = 1

    result = []
    for i in range(len(build)):
        for j in range(len(build[0])):
            if build[i][j] != -1:
                result.append([i, j, build[i][j]])

    result = sorted(result, key= lambda x: (x[0], x[1], x[2]))

    return result

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(5, build_frame))
'''

