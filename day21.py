import sys
sys.stdin=open("input.txt", "r")

'''
2n 번 다른 것과 2n + 1 번 다른 것이 모두 n번 뒤집으면 된다.
'''
from itertools import groupby
s = input()
count = 0
for value, group in groupby(s):
    count += 1
print(count // 2)

'''
그리디 문제
1. 먼저 10의 배수가 아닌거 -1 반환하고
2. 그리디로 각각 세면서 몇인지 저장하면서 한다.
3. join으로 출력
'''
t = int(input())
if t % 10 != 0:
    print(-1)
else:
    times = [300, 60, 10]
    countTimes = []
    for time in times:
        if t // time == 0:
            countTimes.append(str(0))
        else:
            countTimes.append(str(t // time))
            t %= time
    print(' '.join(countTimes))





'''
횟수별 최대 거리
1 = 1
1 1 = 2
1 2 1 = 4
1 2 2 1 = 6
1 2 3 2 1 = 9
1 2 3 3 2 1 = 12
1 2 3 4 3 2 1 = 16
1 2 3 4 4 3 2 1 = 20
1 2 3 4 5 4 3 2 1 = 25

2n - 1, 2n 세트
n * n, n*n + n

몇 거리까지 n번에 갈 수 있나

'''
# t = int(input())

# for _ in range(t):
#     x, y = map(int, input().split())
#     d = y - x
#     n = 1
#     while True:
#         if d <= n * n:
#             print( (n * 2) - 1)
#             break
#         elif d <= n * (n + 1):
#             print(n * 2)
#             break
#         else:
#             n += 1


'''
0층: 1 2 3 4 5 6 7 8 ~ ~
1층: 1 3 6 10
2층: 1 4 10 20
3층: 1 5 15 35
'''
# t= int(input())
# apt = [[0 for _ in range(15)] for _ in range(15)]
# for i in range(1, 15):
#     apt[0][i] = i

# for a in range(1, 15):
#     apt[a][1] = 1
#     for b in range(2, 15):
#         apt[a][b] = sum(apt[a-1][1:b+1])

# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     print(apt[k][n])

# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     apt = [[0] * (n + 1)] * (k + 1)
#     for i in range(1, n + 1):
#         apt[0][i] = i
#     for a in range(1, k + 1):
#         apt[a][1] = 1
#         for b in range(2, n + 1):
#             apt[a][b] = sum(apt[a - 1][1:b + 1])
#     print(apt)



# t = int(input())

# for _ in range(t):
#     h, w, n = map(int, input().split())
#     x = (n - 1) // h + 1
#     y = (n - 1) % h + 1
#     x = str(x) if x > 9 else "0" + str(x)
#     y = str(y)
#     print(y + x)

'''
import math
a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(day)


netDayClimb = a - b
lastClimb = v - (netDayClimb * (v // netDayClimb))

if v - a == 0:
    print(1)
elif ((v - a)//netDayClimb) == 0:
    print(2)
else:
    print(((v - a)//netDayClimb) + 1)
'''



# while True:
#     v -= a
#     count += 1
#     if v <= 0:
#         print(count)
#         break
#     else:
#         v += b

'''
# 홀수의 경우 분자부터
# 짝수의 경우 분모부터

# 1: 0 ~ 2
# 2: 1 ~ 4
# 3: 3 ~ 7

minValue = 0
maxValue = 2
x = int(input())
i = 1

while True:
    if x > minValue and x < maxValue:
        break
    else:
        minValue = maxValue - 1
        maxValue = maxValue + i + 1
        i += 1
count = x - minValue
if i % 2 == 0:
    print(f"{1 + count - 1}/{i - count + 1}")
else:
    print(f"{i - count + 1}/{1 + count - 1}")


# i = 1 / 1
# i = 2 / 2 ~ 7 : 6개
# i = 3 / 8 ~ 19 : 12개
# i = 4 / 20 ~ 37 : 18개
# i = 5 / 38 ~ 61 : 24개
# i = (거리)
# 6 * (i - 1) + 1 ~ (6 * i )+ 1

n = int(input())
i = 1
minNum = 0
maxNum = 1

while True:
    if n >= minNum and n <= maxNum:
        print(i)
        break
    else:
        minNum = maxNum + 1
        maxNum = maxNum + 6 * i
        i += 1




n = int(input())

maxFive = n // 5

for i in range(maxFive, -1, -1):
    if (n - (i * 5)) % 3 == 0:
        ans = i + ((n - (i * 5)) // 3)
        print(ans)
        break
    elif i == 0:
        print(-1)


총비용 = A + B * 생산량
매출 = C * 생산량
A + B * 생산량 = C * 생산량
생산량 = A / (C - B)
    올림

import math

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    ans = math.floor(a / (c - b))
    print(ans + 1)



from itertools import groupby

t = int(input())

def isGroupWord(word):
    chars = []
    for value, group in groupby(word):
        chars.append(value)
    charsSet = set(chars)
    if len(chars) == len(charsSet):
        return True
    else:
        return False

count = 0
for _ in range(t):
    word = input()
    if isGroupWord(word):
        count += 1
    else:
        continue
print(count)
'''
# word = input()
# i = 0
# cnt = 0
# while i < len(word):
#     if word[i] == "c" and i + 1 < len(word):
#         if word[i + 1] == "=":
#             cnt += 1
#             i += 2
#         elif word[i + 1] == "-":
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#             i += 1
#     elif word[i] == "d" and i + 1 < len(word):
#         if word[i + 1] == "z" and i + 2 < len(word):
#             if word[i + 2] == "=":
#                 cnt += 1
#                 i += 3
#             else:
#                 cnt += 1
#                 i += 1
#         elif word[i + 1] == "-":
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#             i += 1
#     elif word[i] == "l" and i + 1 < len(word):
#         if word[i + 1] == "j":
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#             i += 1
#     elif word[i] == "n" and i + 1 < len(word):
#         if word[i + 1] == "j":
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#             i += 1
#     elif word[i] == "s" and i + 1 < len(word):
#         if word[i + 1] == "=":
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#             i += 1
#     elif word[i] == "z" and i + 1 < len(word):
#         if word[i + 1] == "=":
#             cnt += 1
#             i += 2
#         else:
#             cnt +=1
#             i += 1
#     else:
#         cnt += 1
#         i += 1

# print(cnt)

# def getSecond(char):
#     if char in "ABC":
#         return 3
#     elif char in "DEF":
#         return 4
#     elif char in "GHI":
#         return 5
#     elif char in "JKL":
#         return 6
#     elif char in "MNO":
#         return 7
#     elif char in "PQRS":
#         return 8
#     elif char in "TUV":
#         return 9
#     elif char in "WXYZ":
#         return 10
#     elif char in "DEF":
#         return 11

# string = input()
# seconds = 0

# for char in string:
#     seconds += getSecond(char)

# print(seconds)

# a, b = input().split()

# reversedA = int(a[::-1])
# reversedB = int(b[::-1])

# print(max(reversedA, reversedB))

# sentence = list(input().split(" "))

# cnt = 0
# for word in sentence:
#     if word == '':
#         continue
#     else:
#         cnt += 1
# print(cnt)


# from itertools import groupby

# string = list(input().upper())
# string.sort()

# maxChar = ""
# maxNum = 0

# for value, group in groupby(string):
#     numOfChar = len(list(group))
#     if numOfChar > maxNum:
#         maxChar = value
#         maxNum = numOfChar
#     elif numOfChar == maxNum:
#         maxChar = "?"
#     else:
#         continue

# print(maxChar)


# t = int(input())

# for _ in range(t):
#     r, s = input().split()
#     r = int(r)
#     for char in s:
#         for _ in range(r):
#             print(char, end="")
#     print()

# alpha = [-1] * 26
# string = input()

# for i in range(len(string)):
#     check = ord(string[i]) - 97
#     if alpha[check] == -1:
#         alpha[check] = i

# for a in alpha:
#     print(a, end=' ')


# n = int(input())
# nums = input()

# ans = 0
# for i in range(n):
#     ans += int(nums[i])
# print(ans)
