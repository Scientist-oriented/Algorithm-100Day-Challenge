import sys
sys.stdin=open("input.txt", "r")

# 기타 레슨
# 파라메트릭 서치
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

s = max(lectures)
e = sum(lectures)
ans = 100000

while s <= e:
    mid = (s + e) // 2
    length = 0
    numOfBlue = 1

    for lecture in lectures:
        if length + lecture <= mid:
            length += lecture
        else:
            numOfBlue += 1
            length = lecture

    if numOfBlue <= M:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
    
            




# # 알약
# import sys
# input = sys.stdin.readline
# dp = [[0 for _ in range(31)] for _ in range(31)]

# for w in range(1, 31):
#     dp[w][0] = 1
# for w in range(1, 31):
#     for h in range(1, 31):
#         if w < h:
#             continue
#         elif w == h:
#             dp[w][h] = dp[w][h - 1]
#         else:
#             dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

# while True:
#     N = int(input())
#     if N == 0:
#         break
#     print(dp[N][N])



# def dfs(n):
#     global result, wholePill
#     if n == 2 * N:
#         result += 1
#         return
    
#     if not stack:
#         wholePill -= 1
#         stack.append("H")
#         dfs(n + 1)
#     else:
#         if wholePill == 0:
#             stack.pop()
#             dfs(n + 1)
#             stack.append("H")
#         else:
#             wholePill -= 1
#             stack.append("H")
#             dfs(n + 1)
#             wholePill += 1
#             stack.pop()

#             stack.pop()
#             dfs(n + 1)
#             stack.append("H")


# while True:
#     N = int(input())
#     if N == 0:
#         break
#     result = 0
#     stack = []
#     wholePill = N
#     dfs(0)
#     print(result)





# # 고기잡이

# # 전체 길이로 구할 수 있는 그물사이즈를 전부 구하고
# # 완전탐색으로 그물을 다 대본다.

# # 그물 총 길이로 그물 종류 구하기
# def getNets(totalLength):
#     edgeLengthes = totalLength // 2
#     nets = []
#     for i in range(1, edgeLengthes):
#         nets.append((i, edgeLengthes - i))
#     return nets

# # 해당 위치에 해당 그물을 칠 수 있는지 여부
# def isNetPossible(r, c, net):
#     if r + net[0] > N or c + net[1] > N:
#         return False
#     else:
#         return True

# # 해당위치에 특정 그물을 쳐서 얻을 수 있는 물고기 수
# def getFish(r, c, net):
#     if not isNetPossible(r, c, net):
#         return 0

#     fishNum = 0
#     for fish in fishLocations:
#         fr, fc = fish
#         if r <= fr <= r + net[0] and c <= fc <= c + net[1]:
#             fishNum += 1
#     return fishNum
    
# # 해당 그물로 얻을 수 있는 최대 물고기 수
#     # 그물을 모든 위치에 치면 안된다 = 시간초과
# def getMaxFish(net):
#     maxFish = 0
#     for fish in fishLocations: 
#         r, c = fish
#         # 물고기가 항상 꼭지점에만 있으리라는 보장은 없다.
#             # 해당 물고기라 좌, 우 모서리에 오는 모든 케이스를 따져봐야 한다.
#         for nr in range(r, r - net[0] - 1, -1):
#             maxFish = max(maxFish, getFish(nr, c, net))
#         for nc in range(c, c - net[1], -1):
#             maxFish = max(maxFish, getFish(r, nc, net))
#     return maxFish

# N, I, M = map(int, input().split())
# fishLocations = []

# # 물고기 표시
# for _ in range(M):
#     r, c = map(int, input().split())
#     fishLocations.append((r, c))

# def solve():
#     nets = getNets(I)
#     ans = 0
#     for net in nets:
#         ans = max(ans, getMaxFish(net))
#     print(ans)

# solve()



# # 다리 만들기
# # 1. 일단 대륙을 찾아야 함
# # 2. 그리고 해안가 (0과 접한 1)에서 bfs로 다리를 찾는다.
# # 3. 전부 찾아서 길이 최솟값

# from collections import deque

# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

# continents = [[0 for _ in range(N)] for _ in range(N)]

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def isPossible(r, c):
#     if r < 0 or r > N - 1 or c < 0 or c > N - 1:
#         return False
#     else:
#         return True

# # 해안가 인지 확인
# def isShore(r, c):
#     if board[r][c] == 0:
#         return False
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if isPossible(nr, nc) and board[nr][nc] == 0:
#             return True
#     return False

# # 대륙에 번호 붙이기
# def dfs(r, c, continentNum):
#     stack = []
#     visited = [[False for _ in range(N)] for _ in range(N)]

#     stack.append((r, c))
#     visited[r][c] = True
#     continents[r][c] = continentNum

#     while stack:
#         r, c = stack.pop()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isPossible(nr, nc) and board[nr][nc] == 1 and not visited[nr][nc]:
#                 stack.append((nr, nc))
#                 visited[nr][nc] = True
#                 continents[nr][nc] = continentNum

# def bfs(r, c):
#     dq = deque()
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     startingContinent = continents[r][c]

#     dq.append((r, c, 0))
#     visited[r][c] = True

#     while dq:
#         r, c, cost = dq.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isPossible(nr, nc) and board[nr][nc] == 1 and continents[nr][nc] != startingContinent:
#                 # print(f"({r}, {c}) -> ({nr}, {nc}) = {cost}")
#                 # print(f"continent from {startingContinent} to {continents[nr][nc]}")
#                 return cost
#             if isPossible(nr, nc) and not visited[nr][nc] and board[nr][nc] == 0:
#                 dq.append((nr, nc, cost + 1))
#                 visited[nr][nc] = True

#     return 10000
#         # 런타임 에러가 나와서 추가함: 섬 안에 호수가 있는 경우 cost가 출력 안될 수 있음

# def solve():
#     ans = 10000
#     continentNum = 1
#     for r in range(N):
#         for c in range(N):
#             if board[r][c] == 1 and continents[r][c] == 0:
#                 dfs(r, c, continentNum)
#                 continentNum += 1

#     for r in range(N):
#         for c in range(N):
#             if isShore(r, c):
#                 ans = min(ans, bfs(r, c))

#     print(ans)

# solve()




    
# # 차이를 최대로
# from itertools import permutations

# def oper(nums):
#     return sum(abs(nums[i] - nums[i + 1]) for i in range(N - 1))

# N = int(input())
# nums = list(map(int, input().split()))
# ans = 0

# for permu in permutations(nums, N):
#     ans = max(ans, oper(list(permu)))

# print(ans)

# # 가운데를 말해요
# import heapq as hq
# import sys

# N = int(input())
# maxHeap = [] # 중간값 보다 작은 수를 저장한다.
# minHeap = [] # 중간값 보다 큰 수를 저장한다.

# # 이 값을 저장하는 이유는 heap이 비었을 때 pop하면 에러가 나지 않기 위해
#     # 중간값을 구하는데 영향이 없는 범위 외 값들을 하나씩 넣어준다
# hq.heappush(minHeap, 10001)
# hq.heappush(maxHeap, 10001)

# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if len(maxHeap) == len(minHeap):
#         # 두개 힙의 길이가 동일할 때
#             # 각 힙에서 하나씩 뽑아서 현재 입력과 비교한다.
#         nums = [num]
#         nums.append(-hq.heappop(maxHeap))
#         nums.append(hq.heappop(minHeap))
#         nums.sort()

#         # 중간값 출력
#         print(nums[1])

#         # 각 힙의 정의에 맞게 수를 넣고 minHeap에 중간값 저장한다.
#         hq.heappush(maxHeap, -nums[0])
#         hq.heappush(minHeap, nums[2])
#         hq.heappush(minHeap, nums[1])

#     else:
#         nums = [num]
#         # 중간값이랑만 비교하면 된다.
#         nums.append(hq.heappop(minHeap))
#         nums.sort()

#         # 가운데 두 수 중에 작은 것 출력
#         print(nums[0])

#         hq.heappush(maxHeap, -nums[0])
#         hq.heappush(minHeap, nums[1])

# import sys
# import heapq

# N = int(input())
# maxHeap = []
# minHeap = []

# for _ in range(N):
#     n = int(sys.stdin.readline())
#     if len(maxHeap) == len(minHeap):
#         heapq.heappush(maxHeap, -n)
#     else:
#         heapq.heappush(minHeap, n)

#     if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
#         toMin = -heapq.heappop(maxHeap)
#         toMax = heapq.heappop(minHeap)
#         heapq.heappush(minHeap, toMin)
#         heapq.heappush(maxHeap, -toMax)

#     print(-maxHeap[0])