import sys
sys.stdin=open("input.txt", "r", encoding='UTF8')

a, b, v = map(int, input().split())

climbPerDay = a - b

day = (v - a) // climbPerDay

if (v - a) % (a - b) == 0:
    day += 1
else:
    day += 2

print(day)



# # 데이터 받기
# n = int(input())
# meetings = []
# for _ in range(n):
#     s, e = map(int, input().split())
#     meetings.append([s, e])

# # 정렬
# meetings.sort(key=lambda x: (x[1], x[0]))

# # 처음에는 미팅 아무것도 없으니까 끝나는 시간 0, 갯수 0
# endTime = 0
# cnt = 0

# for meeting in meetings:
#     if meeting[0] >= endTime: # 다음 미팅 시작이 현재 스케줄의 끝나는 시간 보다 나중이라면 (혹은 같다면)
#         cnt += 1 # 미팅 추가하고
#         endTime = meeting[1] # 스케줄에 추가한 미팅의 끝나는 시간 반영

# print(cnt)

# l = [1, 2, 3]

# for a in l:
#     print(a)
#     l.remove(a)

# from itertools import permutations
# possibleCases = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# def getStrikeAndBall(givenCase, possibleCase):
#     strike = 0
#     ball = 0
#     possibleCase = list(possibleCase)
#     for i in range(3):
#         if givenCase[i] in possibleCase:
#             if i == possibleCase.index(givenCase[i]):
#                 strike += 1
#             else:
#                 ball += 1
#     return strike, ball

# n = int(input())

# for _ in range(n):
#     num, s, b = map(int, input().split())
#     givenCase = [int(i) for i in str(num)]
#     removeCount = 0
#     for i in range(len(possibleCases)):
#         i = i - removeCount
#         possibleStrike, possibleBall = getStrikeAndBall(givenCase, possibleCases[i])
#         if possibleStrike != s or possibleBall != b:
#             possibleCases.remove(possibleCases[i])
#             removeCount += 1

# print(len(possibleCases))
    

# from itertools import combinations

# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
# cnt = 0

# for i in range(1, n + 1):
#     for combi in combinations(nums, i):
#         if sum(combi) == s:
#             cnt += 1

# print(cnt)

# from itertools import permutations

# possibleCases = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(possibleCases)
    

# # 수직선 만들어서 111 ~ 999까지 체크
# # 반복문 많이 쓰면 어려우니까 볼, 스트라이크 체크 따로따로
# # 볼 스트라이크 각 함수는 tryNum이랑 checkNum을 둘 다 받아서 하는 것으로

# checkNumbers = [0] * 1000

# def checkStrike(tryNum, checkNum, strike):
#     global checkNumbers
#     tryNum = str(tryNum)
#     if "0" in str(checkNum):
#         return
#     if strike == 1:
#         for i in range(3):
#             if tryNum[i] == str(checkNum)[i]:
#                 checkNumbers[checkNum] += 1
#     elif strike == 2:
#         for a, b in [(0, 1), (1, 2), (0, 2)]:
#             if tryNum[a] == str(checkNum)[a] and tryNum[b] == str(checkNum)[b]:
#                 checkNumbers[checkNum] += 1
#     else:
#         return

# def checkBall(tryNum, checkNum, ball):
#     global checkNumbers
#     tryNum = str(tryNum)
#     if "0" in str(checkNum):
#         return
#     if ball == 1:
#         for i in range(3):
#             if tryNum[i] in str(checkNum):
#                 checkNumbers[checkNum] += 1
#     elif ball == 2:
#         for a, b in [(0, 1), (1, 2), (0, 2)]:
#             if tryNum[a] in str(checkNum) and tryNum[b] in str(checkNum):
#                 checkNumbers[checkNum] += 1
#     else:
#         return

# n = int(input())

# for _ in range(n):
#     tryNum, strike, ball = map(int, input().split())
#     for checkNum in range(111, 1000):
#         checkStrike(tryNum, checkNum, strike)
#         checkBall(tryNum, checkNum, ball)

# mostResult = max(checkNumbers)
# cnt = 0

# for i in range(len(checkNumbers)):
#     if checkNumbers[i] == mostResult:
#         cnt += 1

# print(max(checkNumbers))
# print(checkNumbers)
# print(cnt)


# result = [0] * 1000

# n = int(input())

# def checkStrike(tryNum, strike):
#     if strike == 0:
#         return
#     elif strike == 1:
        
#             for j in range(111, 1000):
#                 if "0" in str(result[j]):
#                     pass
#                 else:
#                     if tryNum[i] in str(result[j][i]):
#                         result[j] += 1
#     else:
#         for a, b in [(0, 1), (1, 2), (0, 2)]:
#             for x in range(111, 1000):
#                 if "0" in str(result[x]):
#                     pass
#                 else:
#                     if tryNum[a] == str(result[x])[a] and tryNum[b] == str(result[x])[b]:
#                         result[x] += 1

# def checkBall(tryNum, ball):
#     if ball == 0:
#         return
#     elif ball == 1:
#         for i in range(len(tryNum)):
#             for j in range(111, 1000):
#                 if "0" in str(result[j]):
#                     pass
#                 else:
#                     if tryNum[i] in str(result[j]):
#                         result[j] += 1
#     else:
#         for a, b in [(0, 1), (1, 2), (0, 2)]:
#             for x in range(111, 1000):
#                 if "0" in str(result[x]):
#                     pass
#                 else:
#                     if tryNum[a] in str(result[x])[a] and tryNum[b] == str(result[x])[b]:
#                         result[x] += 1



# def checkPossibleNums(tryNum, strike, ball):
#     if strike > 0:
#         for 

# for _ in range(n):
    # 숫자 판별해서 +1

# from itertools import permutations

# n = int(input())
# nums = [i for i in range(1, n + 1)]


# for permutation in permutations(nums, n):
#     for num in permutation:
#         print(num, end=" ")
#     print()
