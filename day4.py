import sys
sys.stdin=open("input.txt", "r")

# 이취코 p.149
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    # 띄어쓰기가 되어 있지 않은 input은 split없이 쓰면 하나하나 list의 원소로 받을 수 있다.
    # 왜냐면 어차피 string이 iterable이기 때문에 문자 하나하나가 map의 대상이 된다.

def dfs(x, y, count):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        count += 1
        print(x, y, "Out", count)
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        count += 1
        print(x, y, "Land", count)
        dfs(x - 1, y, count)
        dfs(x, y - 1, count)
        dfs(x + 1, y, count)
        dfs(x, y + 1, count)
        return True
    count += 1
    print(x, y, "noland", count)
    return False

a = dfs(0, 0, 0)
print(a)


# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             print(i, j, "Found")
#             result += 1

# print(dfs(0, 0))
# print(dfs(0, 1))
# print(dfs(0, 2))
# print(dfs(1, 0))
# print(dfs(1, 1))
# print(dfs(1, 2))
# print(dfs(2, 0))
# print(dfs(2, 1))
# print(dfs(2, 2))
# print(result)


'''
# 이취코 bfs 구현 p.143
    # dfs는 재귀함수 자체가 스택으로 실행되어서 따로 스택을 구성할 필요가 없었지만
    # bfs는 별로도 queue를 구성해야 한다.

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
'''