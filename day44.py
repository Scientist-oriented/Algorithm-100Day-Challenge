# 돌 게임 3
'''
1. 정의
    f(i) = 돌이 i개 있을 때 이기는 사람
2. 구하는 답
    f(N)
3. 초깃값
    f(1) = SK
    f(2) = CY
    f(3) = SK
    f(4) = SK
4. 점화식
    if f(i - 1) == CY or f(i - 2) == CY or f(i - 4) == CY:
        f(i) = SK
    else:
        f(i) = CY
'''

# Maximum Subarray
'''
1. 정의
    f(i) = 배열의 i번째 인덱스까지의 최대 부분배열의 합
2. 구하는 답
    f(N - 1)
3. 초깃값
    f(0) = arr[0]
4. 점화식
    f(i) = max(arr[i], f(i - 1) + arr[i])
'''

import sys
sys.stdin=open("input.txt", "r")

n = int(input())
cache = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(1, 10):
    cache[1][i] = 1

for i in range(2, n + 1):
    for j in range(0, 10):
        if j == 0:
            cache[i][j] = cache[i - 1][1]
        elif j == 9:
            cache[i][j] = cache[i - 1][8]
        else:
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j + 1]

print(sum(cache[n])/1000000000)

'''
1. 정의
    f(i) = 3×i 크기의 벽 주어진 타일로 채우는 경우의 수
2. 구하는 답
    f(N)
3. 초기값
    f(1) = 0
    f(2) = 3
    f(3) = 0
    f(4) = 8
4. 점화식
    if i == 홀수:
        f(i) = 0
    else:
        f(i) = f(i - 2) * 3 -> f(i - 2)에 3가지 블록 조합을 더하는 경우
        for j in range(4, i - 4, 2):
            f(i) += f(j) * 2 -> 나눌 수 없는 f(4), f(6) 블록을 f(i - 4), f(i - 6)에 붙이는 경우
'''