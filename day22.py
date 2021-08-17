import sys
sys.stdin=open("input.txt", "r", encoding='UTF8')

# 적의 위치 (a, b)라고 했을 때
    # 같은 거리 내의 점들의 집합 = 원

    # 간단히 생각하면 원의 접점의 갯수 만큼
    # 무한대인 경우는 둘의 좌표가 동일한 경우 (예외처리)

    # 접점 2개 : 두 터렛 사이의 거리가 반지름의 합 보다 짧은 경우
    # 접점 1개 : 두 터렛의 사이의 거리가 반지름의 합과 같은 경우
    # 접점 0개 : 두 터렛 사이의 거리가 반지름의ㅇ긴경우

    # 예외 처리 : 한 원이 다른 원 안에 들어간 경우

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    if x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    if distance < r1 + r2:
        print(2)
    elif distance > r1 + r2:
        print(0)
    else:
        print(1)

    


'''
import math

# 길이가 루트(2 * R ** 2)인 정사각형의 넓이 = 2 * R ** 2
r = int(input())
print((r ** 2) * math.pi)
print(2 * (r ** 2))


while True:
    lengths = list(map(int, input().split()))
    if lengths[0] == 0:
        break
    else:
        lengths.sort()
        if lengths[2] ** 2 == lengths[1] ** 2 + lengths[0] ** 2:
            print("right")
        else:
            print("wrong")
'''


# 직사각형을 만들기 위해서는 같은 x좌표 2쌍, 같은 y 좌표 2쌍
# xlist = []
# ylist = []

# for _ in range(3):
#     x, y = map(int, input().split())
#     xlist.append(x)
#     ylist.append(y)

# for x in xlist:
#     if xlist.count(x) == 1:
#         targetX = x
#         break

# for y in ylist:
#     if ylist.count(y) == 1:
#         targetY = y
#         break

# print(targetX, targetY)


# case = 0

# while True:
#     case += 1
#     l, p, v = map(int, input().split())
#     if l == 0:
#         break
#     else:
#         result = 0
#         result += (v // p) * l
#         result += min(v % p, l)
#         print(f"Case {case}: {result}")

'''
1 : 1
2 : 2
3 : 1 2
4 : 2 2
5 : 2 3
6 : 1 2 3
~
10 : 1 2 3 4
~
15 : 1 2 3 4 5

6보다 작으면 2개
2 * (2 + 1) / 2 보다 작으면 1개
i * (i + 1) / 2 보다 작으면 i - 1개


    s = int(input())
    i = 1

    while True:
        if s < (i * (i + 1) / 2):
            print(i - 1)
            break
        else:
            i += 1

'''

# coins = [500, 100, 50, 10, 5, 1]
# price = int(input())
# remainder = 1000 - price

# count = 0

# for coin in coins:
#     count += remainder // coin
#     remainder %= coin

# print(count)