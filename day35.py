import sys
sys.stdin=open("input.txt", "r")

'''
# 처음에 실패한 이유
    : 처음에는 큐에 board를 자체를 저장했다. (deepcopy해서)
    : 그리고 bfs를 실시했다.
        : (테스트 케이스 1번은 통과했다.)
    : 하지만 visited 배열을 전부 순회해야하고 board 둘이 같은지 비교하는 과정이 복잡해서
        : 솔직히 시간초과가 나오고 문제는 풀릴 것이라고 생각했다.
    : 퍼즐을 풀 수 없는 상황에서 무한 루프가 나오는 바람에 안되었다.
        : 아직도 원인은 모르겠다...
    : 결국은 블로그 참고

# 블로그에서 얻은 아이디어
    : 일단 bfs를 실행하는 것은 맞았다.
    : 또한 역시 빈칸 (0) 하나를 저장하는 것이 아니라 board 전체를 저장하는 것도 맞았다.

    : 하지만 board를 큐에 저장하기 위해서 이차원 리스트를 String으로 바꾸었다.
        : 메모리를 아끼고 비교를 편하게 하기 위해서
    : 그리고 visited는 단순한 배열을 사용하면 탐색이 오래 걸리기 때문에
        : hash table (dictionary)를 사용했다. -> 탐색이 O(1)

    : 그리고 queue에 너무 많이 넣어도 안된다...
        : 편의를 위해서 x, y, t까지 넣었는데 메모리 초과 떠서
        : x, y는 board를 통해서 계산하고 t는 hash table에 저장

# 의사 코드
    1. 입력을 받는데 2차원 리스트를 String으로 바꾼다.
    2. dict를 하나 선언해서 key는 string으로 바꾼 board, value는 수를 이동시킨 횟수를 저장한다.
    3. 처음 board를 queue에 넣고 dict에도 넣는다.
    4. bfs를 실시한다.
        4-1. queue에서 나온 board를 바탕으로 빈칸(= 0)의 x, y좌표를 구하고
        4-2. 그 좌표를 바탕으로 동서남북 완전탐색을 실시한다.
        4-3. 수를 이동시킨 board가 dict에 key에 없으면 큐에 넣고 dict에 횟수 표시한다.
    5. 4를 실시하던 중에 원하는대로 정렬되면 dict에서 횟수를 출력하고 큐가 빌 때까지 못찾으면 -1를 출력한다.
'''
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def boardToString(board):
    result = ""
    for i in range(3):
        for j in range(3):
            result += str(board[i][j])
            # 🚫 처음에 여기서 [j][i]로 해서 오타남... -> 함수 점검하기!
    return result

def isValid(x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        return True
    else:
        return False

def changeCoord(b, x1, y1, x2, y2):
    b = list(b)
    index1 = y1 * 3 + x1
    index2 = y2 * 3 + x2
    b[index1], b[index2] = b[index2], b[index1]
    return ''.join(b)

def bfs(board):
    dq = deque()
    visited = dict()

    dq.append(board)
    visited[board] = 1

    while dq:
        b = dq.popleft()
        if b == answer:
            print(visited[b] - 1)
            return
        x = b.find('0') % 3
        y = b.find('0') // 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny):
                nb = changeCoord(b, x, y, nx, ny)
                if not visited.get(nb):
                    # 💡 visited[key]로 접근하면 key 없으면 에러남, get은 none을 반환함!
                    dq.append((nb))
                    visited[nb] = visited[b] + 1
    
    print(-1)
    return

board = [list(map(int, input().split())) for _ in range(3)]
answer = "123456780"
board = boardToString(board)
bfs(board)





# from collections import deque
# import copy

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def isAnswer(board):
#     answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#     for i in range(3):
#         for j in range(3):
#             if board[j][i] != answer[j][i]:
#                 return False
#     return True

# def isSame(b1, b2):
#     for i in range(3):
#         for j in range(3):
#             if b1[j][i] != b2[j][i]:
#                 return False
#     return True

# def isValid(x, y):
#     if 0 <= x < 3 and 0 <= y < 3:
#         return True
#     else:
#         return False

# def bfs(x, y, board):
#     dq = deque()
#     visited = []

#     dq.append((x, y, 0, board))
#     visited.append(board)

#     while dq:
#         x, y, t, b = dq.popleft()
#         if x == y == 2 and isAnswer(b):
#             print(t)
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if isValid(nx, ny):
#                 nb = copy.deepcopy(b)
#                 nb[y][x], nb[ny][nx] = nb[ny][nx], nb[y][x]
#                 isVisit = False
#                 for vb in visited:
#                     if isSame(vb, nb):
#                         isVisit = True
#                         break
#                 if not isVisit:
#                     dq.append((nx, ny, t + 1, nb))                
#                     visited.append(nb)

#     print(-1)
#     return

# board = [list(map(int, input().split())) for _ in range(3)]

# for i in range(3):
#     for j in range(3):
#         if board[j][i] == 0:
#             bfs(i, j, board)


'''
# 사용해야 하는 알고리즘 = bfs
    : bfs를 사용하는 문제의 패턴 = 몇가지 선택지 + 최단시간
    : 이 문제도 마찬가지로 D, S, L, R의 4가지 명령어 버튼을 조작해서 최단시간에 탈출

# 문제 풀이 아이디어
    : 전형적인 bfs 문제인데
    : 명령어 부분에서 문자열을 조작하는 것이 좀 까다롭다.
        : 1000보다 작은 수의 경우에는 문자열로 변환할 때
        : 1 -> 0001 이런 식으로 빈 자릿수에 0을 채워햐 한다.

# 의사 코드
    1. 각 명령어에 해당하는 함수를 미리 구현해 놓는다.
    2. 빈 큐를 선언하고 방문 체크를 위한 배열을 선언한다.
    3. 큐에 (A, "")을 넣고 bfs를 수행한다.
        3-1. A == B이면 문자열을 출력한다.
        3-2. A를 DSLR 각각의 연산에 대해 완전탐색을 실시한다.
            3-2-1. 연산결과가 방문이 안되었다면
            3-2-2. 큐에 (연산결과, 기존문자열 + "추가된 연산")을 넣는다.
'''
# from collections import deque

# def D(n):
#     return (n * 2) % 10000

# def S(n):
#     return n - 1 if n > 0 else 9999

# def L(n):
#     n = str(n)
#     if len(n) < 4:
#         n = ("0" *(4 - len(n))) + n
#     return int(n[1:] + n[0])

# def R(n):
#     n = str(n)
#     if len(n) < 4:
#         n = ("0" *(4 - len(n))) + n
#     return int(n[3] + n[:3])

# commands = [(D, "D"), (S, "S"), (L, "L"), (R, "R")]

# def bfs(A, B):
#     dq = deque()
#     visited = [False for _ in range(10000)]

#     dq.append((A, ""))
#     visited[A] = True
    
#     while dq:
#         now, result = dq.popleft()
#         if now == B:
#             print(result)
#             return
#         for i in range(4):
#             next = commands[i][0](now)
#             if not visited[next]:
#                 dq.append((next, result + commands[i][1]))
#                 visited[next] = True
     

# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     bfs(A, B)


'''
# 사용해야 하는 알고리즘 = bfs
    : bfs를 사용하는 문제의 패턴 = 몇가지 선택지 + 최단시간
    : 이 문제도 마찬가지로 A, B 2가지 버튼을 조작해서 최단시간에 탈출

# 문제 풀이 아이디어
    : 방문체크를 위한 수직선을 만들고
    : 버튼을 t번 조작한 숫자에 대해 A, B 경우의 수를 완전 탐색한다.

# 의사코드
    1. 입력을 받고 빈 큐와 방문체크 배열을 선언한다.
    2. buttonB를 미리 함수로 만들어 둔다.
        2-1. 입력을 받아 2배를 하고 (99999 넘는지 확인)
        2-2. String으로 타입 변환하고 n[0]에서 1을 뺀 후
        2-3. n[0] + n[1:]을 다시 정수로 바꾸어 반환한다.
        2-4. 반환하는 값이 조건에 맞는지도 확인! (음수가 나올 수도 있음)
    3. 빈 큐에 (N, t(= 0))을 넣고 bfs를 실시한다.
        3-1. 큐에서 나온 시간 > T이면 문자열을 출력하고 멈춘다.
        3-2. 큐에서 나온 수 == G이면 t를 출력하고 멈춘다.
        3-3. 각각 버튼 A를 누른 경우와 B를 누른 경우에 대해 완전탐색한다.
'''
# from collections import deque
# N, T, G = map(int, input().split())

# def buttonB(n):
#     n *= 2
#     if n > 99999:
#         return "not valid"
#     n = str(n)
#     temp = str(int(n[0]) - 1)
#     n = temp + n[1:]
#     return int(n) if 0 <= int(n) < 100000 else "not valid"
#     # 🚫 여기 최종값을 검증을 안해서 0이 들어오면 -1이 나왔다.
#         # 계속 valueError가 떴었다.

# def bfs(N, T, G):
#     dq = deque()
#     visited = [False for _ in range(100000)]
#     dq.append((N, 0))
#     visited[N] = True
#     while dq:
#         n, t = dq.popleft()
#         if t > T:
#             print("ANG")
#             return
#         if n == G:
#             print(t)
#             return
#         if 0 <= n + 1 <= 99999 and not visited[n + 1]:
#             dq.append((n + 1, t + 1))
#             visited[n + 1] = True
#         if buttonB(n) != "not valid" and not visited[buttonB(n)]:
#             dq.append((buttonB(n), t + 1))
#             visited[buttonB(n)] = True
#     print("ANG")
#     return    

# bfs(N, T, G)

'''
# 사용해야 하는 알고리즘 = bfs
    : t초 후의 위치에서 앞으로 걷기 / 뒤로 걷기 / 순간이동 세가지 경우에 대해
    : 완전 탐색을 해야하여 최단 거리를 구하면 됨.

# 문제 풀이 아이디어
    : 방문 체크를 하기 위한 수직선을 만들고
    : 수빈이가 이동하는 위치를 방문체크하면서 3가지 이동 케이스를 완전 탐색한다.
    : 동서남북 탐색과 동일한 원리

# 의사코드
    1. 입력을 받고 빈큐와 방문체크용 배열을 선언한다.
    2. 큐에 n과 t(= 0)을 튜플로 만들어서 넣고 bfs를 실시한다.
        2-1. 큐에서 나온 위치가 k와 동일하면 t를 출력한다.
        2-2. 큐에서 나온 위치에 +1 / -1 / *2가 미방문이면 큐에 넣는다.
'''
# from collections import deque
# n, k = map(int, input().split())

# def bfs(n, k):
#     dq = deque()
#     visited = [False for _ in range(100001)]
#     dq.append((n, 0))
#     while dq:
#         n, t = dq.popleft()
#         if n == k:
#             print(t)
#             return
#         if 0 <= n + 1 <= 100000 and not visited[n + 1]:
#             dq.append((n + 1, t + 1))
#             visited[n + 1] = True
#         if 0 <= n - 1 <= 100000 and not visited[n - 1]:
#             dq.append((n - 1, t + 1))
#             visited[n - 1] = True
#         if 0 <= n * 2 <= 100000 and not visited[n * 2]:
#             dq.append((n * 2, t + 1))
#             visited[n * 2] = True
# bfs(n, k)
'''
# 사용해야 하는 알고리즘 = bfs
    : 현재 위치에서 U혹은 D 두가지 방법을 완전 탐색을 하면서
    : 목표층까지 최단 거리를 구해야 한다.

# 문제 풀이 아이디어
    : 이미 방문한 층을 방문 체크를 하면서 
    : U, D 두 가지 경우를 완전탐색하면된다.
    : 인접행렬을 이용한 동서남북 탐색과 근본적인 원리는 동일하다.

# 의사코드
    1. 입력을 받고 길이가 F + 1인 방문체크용 배열을 선언한다.
    2. 큐에 시작위치와 시작시간(= 0)을 튜플로 넣고 bfs를 실시한다.
        2-1. 큐에서 나온 위치가 G와 동일하면 시간 + 1을 출력하고 중단한다.
        2-2. 큐에서 나온 위치에 U, D를 계산해서 방문하지 않은 층은 큐에 넣는다.
    3. 큐가 빌 때까지 G에 도착하지 못하면 "use the stairs"를 출력한다.

# 주의할 점!
    : G에 도착했는지 체크를 큐에서 나오자마자 해야한다!
        : 만약에 U, D를 계산한 후에 하면 시작위치 = 도착위치면 걸린 횟수가 0이 안나온다!
'''
# from collections import deque

# F, S, G, U, D = map(int, input().split())

# moves = [U, -D]
# visited = [False for _ in range(F + 1)]

# dq = deque()
# dq.append((S, 0))
# visited[S] = True
# def bfs():
#     while dq:
#         now, t = dq.popleft()
#         if now == G:
#             print(t)
#             return 
#         for i in range(2):
#             next = now + moves[i]
#             if 1 <= next <= F and not visited[next]:
#                 dq.append((next, t + 1))
#                 visited[next] = True
#     print("use the stairs")

# bfs()
