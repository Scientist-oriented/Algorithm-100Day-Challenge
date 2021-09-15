# 감시
'''
# 자료구조/알고리즘
    : dfs
# 풀이방법
    1. 5번 cctv가 처리할 수 있는 영역을 먼저 표시한다.
    2. 사무실을 완전탐색하면서 cctv를 만날 때 마다 dfs를 실시한다.
    3. dfs를 통해 완전탐색한 후 사각지대의 최솟값을 갱신한다.
'''

# 로또
'''
# 자료구조/알고리즘
    : combination
# 풀이방법
    1. 주어진 집합을 배열에 담고 combination을 활용해서 조합을 구한다.
    2. 조합을 각각 출력한다.
'''
# 이차원 배열과 연산
'''
# 자료구조/알고리즘
    : 구현, counter
# 풀이방법
    1. 각 연산을 counter로 구현한다.
    2. c연산은 r연산을 행 <-> 열 교환해서 하는 것으로 한다.
    3. 반복문으로 조건에 만족할 때까지 실행한다.
'''
# 구슬 찾기
'''
# 자료구조/알고리즘
    : graph
# 풀이방법
    1. 인접배열 N * N을 2개 만들어서 하나는 가벼운 관계를 나타내고 하나는 무거운 관계를 나타낸다.
    2. 완전탐색을 통해서 각 구슬 보다 가벼운, 무거운 구슬을 갯수를 각각 센다.
    3. 가벼운 혹은 무거운 구슬의 갯수가 n / 2 보다 크면 중간이 될 가능성이 전혀 없는 구슬이다.
'''
# 외판원 순회 2
'''
# 자료구조/알고리즘
    : dfs
# 풀이방법
    1. dfs로 방문처리 하면서 모든 경로를 탐색한다.
    2. 처음에 출발한 도시를 저장했다가 마지막에 돌아오는 비용을 추가한다.
    3. 최소 비용을 출력한다.
'''
# 킹
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 이차원 배열로 8 * 8 체스판을 구현한다.
    2. 주어진 입력대로 이동한다.
    3. 최종 위치를 출력한다.
'''

# 거스름돈
'''
# 자료구조/알고리즘
    : 그리디
# 풀이방법
    1. 거스름돈을 가장 큰 동전부터 순서대로 나눈다.
    2. 몫은 동전의 갯수이고 나머지가 남은 잔돈이다.
    3. 남은 잔돈이 0이 될 때까지 반복한다.
'''
# 행렬
'''
# 자료구조/알고리즘
    : 그리디
# 풀이방법
    1. (0, 0)부터 A와 B 행렬을 비교하는 완전탐색을 한다.
    2. 다르면 그 좌표에서 연산을 실시한다.
    3. (N - 2, M - 2)까지 탐색을 마친 결과 총 연산 횟수를 출력한다.
'''

# 주사위 굴리기
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 주사위의 상태를 저장하는 배열을 만든다.
    2. 주사위를 굴릴 때마다 바닥에 오는 면을 방향별로 구해주는 함수를 만든다.
    3. 주사위의 위치를 명령에 따라 옮기면서 주사위 상태를 업데이트한다.
    4. 3을 하면서 윗면을 출력한다.
'''

# 병든 나이트
'''
# 자료구조/알고리즘
    : 규칙 찾기
# 풀이방법
    1. 체스판 높이 1, 2에 대해 규칙을 찾는다.
    2. 체스판 높이 3 이상에 대해서 규칙을 찾는다.
# 솔직히 잘 모르겠다...
'''

# 경로 찾기
'''
# 자료구조/알고리즘
    : dfs
# 풀이방법
    1. 주어진 경로 정보를 바탕으로 i에서 dfs를 실시한다.
    2. 방문이 가능한 node를 1로 표시한다.
'''
# 우리집엔 도서관이 있어
'''
# 자료구조/알고리즘
    : 규칙 찾기
# 풀이방법
    1. N 위에 (어디든) 위치한 N - 1이 위치해 있을 경우 두 책은 정렬할 필요가 없다.
    2. 마찬가지로 N - 2가 N - 1위에 있을 경우 두 책은 정렬할 필요가 없다.
    3. 주어진 책 배열에서 N 위에 있는 탐색하면서 -1씩 하면서 몇권의 책이 정렬할 필요가 없는지 센다.
    4. 정렬할 필요가 없는 책 갯수를 토해서 정렬해야 하는 책을 구한다.
'''
# 경사로
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 각 길을 모두 탐색한다.
    2. 오르막 경사로가 필요한 경우는 L길이의 경사로를 놓을 수 있는지 이전 L - 1칸의 높이가 같은지 확인한다.
    3. 내리막 경사로가 필요한 경우는 L길이의 경사로를 놓을 수 있는지 이후 L칸의 높이가 같은지 확인한다.
    4. 경사로를 놓은 곳에는 표시를 해서 경사로가 겹치지 않도록 한다.
    5. 경사로를 놓았다면 경사로가 끝나는 부분에서 다시 탐색한다.
'''
# 좋은 수열
'''
# 자료구조/알고리즘
    : 백트래킹
# 풀이방법
    1. dfs를 통해서 1 ~ 3까지 앞에 완성된 좋은 수열에 붙여가면서 반복한다.
    2. 완성된 수열이 좋은 수열인지 확인하고 아니면 return한다.
    3. 가장 처음 완성된 N 길이의 좋은 수열을 출력한다.
'''
# 테트로미노
'''
# 자료구조/알고리즘
    : 완전탐색
# 풀이방법
    1. 각 테트로미노 당 회전했을 때 차지하는 좌표를 미리 정해놓는다.
    2. 모든 좌표에서 테트로미노의 종류 * 회전 하는 경우를 완전탐색한다.
    3. 최댓값을 갱신한다.
'''

# 문제 이름
'''
# 자료구조/알고리즘
# 풀이방법
'''

# 구슬 탈출 2
'''
# 자료구조/알고리즘
    : bfs
# 풀이방법
    1. 보드를 이차원 배열로 저장한다.
    2. 왼쪽, 오른쪽, 위, 아래 기울이는 것을 함수로 구현한다.
    3. bfs를 위해 현재 R과 B의 위치 그리고 시도횟수를 묶어서 큐에 넣는다.
    4. bfs를 왼쪽, 오른쪽, 위, 아래에 대해 실시한다.
        : 이 중에 B 구슬이 구멍에 빠지는 경우는 배제한다.
    5. 가장 빨리 R구슬이 떨어지는 시도횟수를 출력한다.
        : 10번 안에 안되면 (= 큐에서 popleft된 경우의 시도횟수가 10이상이면) -1을 출력한다.
'''

import sys
sys.stdin=open("input.txt", "r")

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

def isPossible(limit):
    totalCost = sum(min(budget, limit) for budget in budgets)
    if totalCost <= M:
        return True
    else:
        return False

s = 1
e = max(budgets)
result = s

while s <= e:
    mid = (s + e) // 2

    if isPossible(mid):
        result = max(mid, result)
        s = mid + 1
    else:
        e = mid - 1

print(result)