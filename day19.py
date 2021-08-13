import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rsplit())
    print(a + b)

# n = int(input())
# print(int(n*(n + 1)/2))

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print(a + b)

# n = int(input())

# for a in range(1, 10):
#     print(n, '*', a, '=', n*a)

# h, m = map(int, input().split())


# if m - 45 < 0:
#     if h - 1 < 0:
#         print(23, m + 15)
#     else:
#         print(h - 1, m + 15)
# else:
#     print(h, m - 45)

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# year = int(input())

# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print(1)
# else:
#     print(0)

# score = int(input())

# if score >= 90:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# else:
#     print("F")
# a, b = map(int, input().split())

# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")

# a = int(input())
# b = str(input()) 

# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))


# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)


# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

# a, b = map(int, input().split())
# print(a + b)