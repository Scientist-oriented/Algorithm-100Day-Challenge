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