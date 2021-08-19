import sys
sys.stdin=open("input.txt", "r")



# 베스트 셀러
from collections import Counter
counter = Counter([input() for _ in range(int(input()))])
name = []
amount = counter.most_common()[0][1]
for key in counter.keys():
    if counter[key] >= amount:
        name.append(key)
        amount = counter[key]

name.sort()
print(name[0])

# n = int(input())
# counter = []
# for _ in range(n):
#     counter.append(input())
# counter = Counter(counter)

# # 회사에 있는 사람
# import sys
# n = int(input())
# company = set()
# for _ in range(n):
#     name, action = sys.stdin.readline().rstrip().rsplit(' ')
#     if action == "enter":
#         company.add(name)
#     else:
#         company.remove(name)

# company = list(company)
# company.sort(reverse=True)
# for name in company:
#     print(name)

# # 절댓값 힙
# import heapq
# import sys

# n = int(input())
# heap = []
# for _ in range(n):
#     num = int(sys.stdin.readline().rstrip())
#     if num != 0:
#         pair = (abs(num), num)
#         heapq.heappush(heap, pair)
#     else:
#         print(heapq.heappop(heap)[1] if heap else 0)

# # 카드 2
# from collections import deque
# n = int(input())
# dq = deque(i for i in range(1, n + 1))

# while len(dq) != 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq.popleft())

# # 후위 표기식
# n = int(input())
# string = input()
# stack = []
# nums = [False] * 26

# for i in range(n):
#     nums[i] = int(input())

# for char in string:
#     if char.isalpha():
#         stack.append(nums[ord(char) - ord("A")])
#     else:
#         a = stack.pop()
#         b = stack.pop()
#         if char == "+":
#             stack.append(a + b)
#         elif char == "-":
#             stack.append(b - a)
#         elif char == "*":
#             stack.append(a * b)
#         else:
#             stack.append(b / a)
# print(f"{stack.pop():.2f}")

# # 괄호
# t = int(input())

# def isVPS(string):
#     stack = []
#     for char in string:
#         if char == "(":
#             stack.append(0)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 return False
#     return True if not stack else False

# for _ in range(t):
#     string = input()
#     if isVPS(string):
#         print("YES")
#     else:
#         print("NO")

# # 올바른 괄호 문자열인지 확인 하는 함수
# def isValid(string):
#     stackSmall = []
#     stackMedium = []
#     stackBig = []
#     for char in string:
#         if char == "(":
#             stackSmall.append(0)
#         elif char == ")":
#             if stackSmall and not stackMedium and not stackBig:
#                 stackSmall.pop()
#             else:
#                 return False
#         elif char == "{":
#             stackMedium.append(0)
#         elif char == "}":
#             if stackMedium and not stackSmall and not stackBig:
#                 stackMedium.pop()
#             else:
#                 return False
#         elif char == "[":
#             stackBig.append(0)
#         elif char == "]":
#             if stackBig and not stackSmall and not stackMedium:
#                 stackBig.pop()
#             else:
#                 return False
#     if not stackSmall and not stackMedium and not stackBig:
#         return True
#     else:
#         return False

# # 문자열에 필요한 필수 괄호 구하기

