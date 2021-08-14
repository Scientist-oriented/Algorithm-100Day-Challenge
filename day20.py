import sys
sys.stdin=open("input.txt", "r")

# def isHanSu(x):
#     digits = str(x)
#     if len(digits) == 1:
#         return True
#     digitGap = None
#     for i in range(len(digits) - 2):
#         if int(digits[i]) - int(digits[i + 1]) == int(digits[i + 1]) - int(digits[i + 2]):
#             continue
#         else:
#             return False
#     return True

# n = int(input())
# cnt = 0
# for i in range(1, n + 1):
#     if isHanSu(i):
#         cnt += 1
# print(cnt)



# result = [False] * 10001

# def d(n):
#     digits = str(n)
#     for digit in digits:
#         n += int(digit)
#     return n

# for n in range(1, 10001):
#     if d(n) <= 10000:
#         result[d(n)] = True

# for i in range(1, len(result)):
#     if result[i] == False:
#         print(i)



# def solve(a: list) -> int:
#     return sum(a)

# c = int(input())

# for _ in range(c):
#     scores = list(map(int, input().split()))
#     n = scores.pop(0)
#     avg = sum(scores) / n
#     overAvg = 0
#     for score in scores:
#         if score > avg:
#             overAvg += 1
#     result = round(overAvg / n * 100, 3)
#     print(f"{result:.3f}%")

# t = int(input())

# for _ in range(t):
#     results = input()
#     score = 0
#     cnt = 0
#     for result in results:
#         if result == "O":
#             cnt += 1
#             score += cnt
#         else:
#             cnt = 0
#     print(score)

# n = int(input())
# oldScores = list(map(int, input().split()))
# m = max(oldScores)
# result = ((sum(oldScores) / n) / m) * 100
# print(result)
    

# inputs = set()

# for _ in range(10):
#     remainder = int(input()) % 42
#     inputs.add(remainder)

# print(len(inputs))

# a = int(input())
# b = int(input())
# c = int(input())

# abc = str(a * b * c)

# result = [0] * 10

# for digit in abc:
#     result[int(digit)] += 1

# for i in result:
#     print(i)

# nums = []

# for _ in range(9):
#     nums.append(int(input()))

# maxNum = max(nums)

# print(maxNum)
# print(nums.index(maxNum) + 1)

# n = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers), max(numbers))

# n = int(input())
# x = n

# def addAndReturnFirstDigit(a, b):
#     a, b = int(a), int(b)
#     added = a + b
#     firstDigit = str(added)[-1]
#     return firstDigit

# cnt = 0

# while True:
#     if x > 9:
#         a, b = str(x)[0], str(x)[1]
#         x2 = addAndReturnFirstDigit(a, b)
#         x1 = b
#         x = int(x1 + x2)
#         cnt += 1
#     else:
#         a, b = 0, str(x)[0]
#         x2 = addAndReturnFirstDigit(a, b)
#         x1 = b
#         x = int(x1 + x2)
#         cnt += 1
#     if n == x:
#         print(cnt)
#         break
        


# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break
    

# while True:
#     a, b = map(int, input().split())
#     if a + b == 0:
#         break
#     else:
#         print(a + b)

# n, x = map(int, input().split())
# a = list(map(int, input().split()))

# for i in a:
#     if i < x:
#         print(i, end=' ')


# n = int(input())

# for i in range(1, n + 1):
#     stars = ' ' * (n - i) + '*' * i
#     print(stars)


# n = int(input())

# for i in range(1, n + 1):
#     stars = '*' * i
#     print(stars)

# t = int(input())

# for i in range(1, t + 1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a} + {b} = {a + b}")

# t = int(input())

# for i in range(1, t + 1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a + b}")

# n = int(input())

# for i in range(n, 0, -1):
#     print(i)

# n = int(input())

# for i in range(1, n + 1):
#     print(i)