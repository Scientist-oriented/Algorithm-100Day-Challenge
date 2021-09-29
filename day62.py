import sys
sys.stdin=open("input.txt", "r")

# 카드 짝 맞추기
'''
0, 1, 2, 3 -> 각각 좌상하우
4 5 6 7 -> 각각 ctrl + 좌상하우
'''

from collections import deque
import copy

def move(r, c, command, board):
    if command == 0:
        return r, c - 1 if c - 1 >= 0 else r, c
    elif command == 1:
        return r - 1, c if r - 1 >= 0 else r, c
    elif command == 2:
        return r + 1, c if r + 1 < 4 else r, c
    elif command == 3:
        return r, c + 1 if c + 1 < 4 else r, c
    elif command == 4:
        if c == 0:
            return r, c
        else:
            c -= 1
            while board[r][c] == 0 and c > 0:
                c -= 1
            return r, c
    elif command == 5:
        if r == 0:
            return r, c
        else:
            r -= 1
            while board[r][c] == 0 and r > 0:
                r -= 1
            return r, c
    elif command == 6:
        if r == 3:
            return r, c
        else:
            r += 1
            while board[r][c] == 0 and r < 3:
                r += 1
            return r, c
    elif command == 7:
        if c == 3:
            return r, c
        else:
            c += 1
            while board[r][c] == 0 and c < 3:
                c += 1
            return r, c

def findSameCard(r, c, board):
    for sr in range(4):
        for sc in range(4):
            if board[sr][sc] == board[r][c]:
                return sr, sc

def costToNextPosition(r, c, sr, sc, board):
    visited = [[False for _ in range(4)] for _ in range(4)]
    dq = deque()
    
    dq.append((r, c, 0))
    visited[r][c] = True

    while dq:
        r, c, cost = dq.popleft()
        if r == sr and c == sc:
            return cost
        
        for i in range(8):
            print(r, c, move(r, c, i, board))
            nr, nc = move(r, c, i, board)
            if not visited[nr][nc]:
                dq.append((nr, nc, cost + 1))
                visited[nr][nc] = True

def findLeftCards(board):
    result = []
    for r in range(4):
        for c in range(4):
            if board[r][c] > 0:
                result.append((r, c))
    return result

def oneCycle(r1, c1, r2, c2):
    r, c = r1, c1
    cost = 0

    # 처음 고른 카드위치까지
    cost += costToNextPosition(r1, c1, r2, c2, board)
    r, c = r2, c2

    # 엔터 누름
    cost += 1

    # 다음 목적지 찾기
    sr, sc = findSameCard(r, c)

    # 처음 고른 카드와 같은 카드까지
    cost += costToNextPosition(r, c, sr, sc)
    r, c = sr, sc

    # 엔터누름
    cost += 1

    return r, c, sr, sc, cost

def dfs(r, c, cost, board):
    leftCards = findLeftCards(board)
    
    global ans
    if not leftCards:
        ans = min(ans, cost)
        return

    for card in leftCards:
        card1R, card1C = card
        card2R, card2C = findSameCard(card1R, card1C, board)
        nr, nc, addedCost = oneCycle(r, c, card1R, card1C)
        temp = copy.deepcopy(board[card1R][card1C])
        board[card1R][card1C] = 0
        board[card2R][card2C] = 0
        cost += addedCost
        dfs(nr, nc, cost, board)
        board[card1R][card1C] = temp
        board[card2R][card2C] = temp
        cost -= addedCost

def solution(board, r, c):
    ans = 9999999999
    board = board
    dfs(r, c, 0, board)
    return ans

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

print(solution(board, r, c))

# # 순위 검색
# '''
# 개발언어 0 1 2
# 직군 
# '''

# def personToDataFormat(person):
#     person = person.split(' ')
#     key = person[0] + person[1] + person[2] + person[3]
#     value = int(person[4])
#     return key, value

# def infoToDB(info):
#     db = dict()
#     for person in info:
#         key, value = personToDataFormat(person)
#         if key not in db:
#             db[key] = []
#             db[key].append(value)
#         else:
#             db[key].append(value)
#     return db

# def refineQuery(query):
#     return "" if query == "-" else query

# def removeAnd(query):
#     for _ in range(3):
#         query.remove("and")
#     return query

# def findFromDB(db, query):
#     query = query.split(' ')
#     query = removeAnd(query)
#     query = map(refineQuery, query)
#     lang, job, career, food, score = query
#     result = []
#     for key in db.keys():
#         if lang in key and job in key and career in key and food in key:
#             result.extend(db[key])
#     result = list(filter(lambda x: x >= int(score), result))

#     return len(result)

# def solution(info, query):
#     db = infoToDB(info)
#     answer = []
#     for q in query:
#         answer.append(findFromDB(db, q))
#     return answer
    
# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(info, query))



# from itertools import combinations

# def getMenuList(orders):
#     result = []
#     for order in orders:
#         result.extend(list(order))
#     return list(set(result))

# def makeSetCandidates(menuList, courseVolume):
#     result = []
#     for combi in combinations(menuList, courseVolume):
#         result.append(list(combi))
#     return result

# def getPopularity(orders, candidate):
#     result = 0
#     candidate = set(candidate)
#     for order in orders:
#         if candidate == candidate.intersection(set(order)):
#             result += 1
#     return result

# def decideCourse(menuList, orders, courseVolume):
#     result = []
#     maxSell = 0
#     candidates = makeSetCandidates(menuList, courseVolume)
#     for candidate in candidates:
#         popularity = getPopularity(orders, candidate)
#         if popularity > maxSell:
#             result = []
#             result.append(candidate)
#             maxSell = popularity
#         elif popularity == maxSell:
#             result.append(candidate)
#     return result if maxSell > 1 else []

# def organizeAns(results):
#     answer = []
#     for result in results:
#         result = sorted(result)
#         result = ''.join(result)
#         answer.append(result)
#     return sorted(answer)


# def solution(orders, course):
#     menuList = getMenuList(orders)

#     result = []
#     for courseVolume in course:
#         courseResult = decideCourse(menuList, orders, courseVolume)
#         result.extend(courseResult)

#     return organizeAns(result)

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]

# print(solution(orders, course))

# 메뉴 리뉴얼

# # 신규 아이디 추천
# def phase1(new_id: str):
#     new_id = list(new_id)
#     for i in range(len(new_id)):
#         if new_id[i].isupper():
#             new_id[i] = new_id[i].lower()
#     return ''.join(new_id)

# def phase2(new_id):
#     allowedChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", "_", "."]
#     result = ""
#     for char in new_id:
#         if char in allowedChar:
#             result += char
#     return result

# def phase3(new_id):
#     idx = 0
#     result = ""
#     while idx < len(new_id):
#         if new_id[idx] != ".":
#             result += new_id[idx]
#             idx += 1
#         else:
#             result += "."
#             while idx < len(new_id) and new_id[idx] == ".":
#                 idx += 1
#     return result

# def phase4(new_id: str):
#     if new_id and new_id[0] == ".":
#         new_id = new_id[1:]
#     if new_id and new_id[-1] == ".":
#         new_id = new_id[:-1]
#     return new_id

# def phase5(new_id):
#     return "a" if new_id == "" else new_id

# def phase6(new_id):
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         if new_id[-1] == ".":
#             new_id = new_id[:-1]
            
#     return new_id

# def phase7(new_id):
#     if len(new_id) <= 2:
#         addedChar = new_id[-1]
#         while len(new_id) < 3:
#             new_id += addedChar
#     return new_id

# def solution(new_id):
#     afterOne = phase1(new_id)
#     afterTwo = phase2(afterOne)
#     afterThree = phase3(afterTwo)
#     afterFour = phase4(afterThree)
#     afterFive = phase5(afterFour)
#     afterSix = phase6(afterFive)
#     afterSeven = phase7(afterSix)

#     return afterSeven

# print(solution("...!@BaT#*..y.abcdefghijklm"))


# # 비슷한 단어

# def asc(char):
#     return ord(char) - ord("A")

# def isSimiliar(word1, word2):
#     check = [0 for _ in range(26)]
#     for char1 in word1:
#         check[asc(char1)] += 1

#     for char2 in word2:
#         check[asc(char2)] -= 1

#     plus = 0
#     minus = 0

#     for c in check:
#         if c > 0:
#             plus += c
#         elif c < 0:
#             minus -= c

#     return True if plus < 2 and minus < 2 else False

# N = int(input())
# word1 = input()
# words = []
# for _ in range(N - 1):
#     words.append(input())

# ans = 0

# for word2 in words:
#     if isSimiliar(word1, word2):
#         #print(word1, word2, isSimiliar(word1, word2))
#         ans += 1

# print(ans)

# print("---------debug------------")
# a = "A"
# b = "B"
# print(isSimiliar(a, b))



# # 사전
# def solve(N, M, K):
#     dp = [[1 for _ in range(M + 1)] for _ in range(N + 1)]

#     # 중복순열
#     for a in range(1, N + 1):
#         for z in range(1, M + 1):
#             dp[a][z] = dp[a - 1][z] + dp[a][z - 1]

#     # dp[N][M] = a N개와 z M개로 만들 수 있는 문자열의 갯수
#     if dp[N][M] < K:
#         print(-1)
#         return

#     # k를 가지고 문자열의 첫번째 자리부터 정해나가는 것
#     ans = ""
#     a, z, k = N, M, K
#     while True:
#         # a, z 중 하나가 0개 남았을 때 = 남은 문자열 채워 넣기
#         if a == 0 or z == 0:
#             ans += "a" * a
#             ans += "z" * z
#             break
        
#         # 첫 자리가 a로 시작하는 경우 문자열의 갯수
#         startFromA = dp[a - 1][z]

#         # k번째가 첫자리가 a로 시작할 수 있는 경우
#         if k <= startFromA:
#             ans += "a"
#             a -= 1
#         # k번째가 첫자리가 a로 시작할 수 없는 경우
#         else:
#             ans += "z"
#             z -= 1
#             k -= startFromA # z로 시작했으므로 다음번에는 z로 시작한 첫번째 순서를 구하기 위해 뺀다 
    
#     print(ans)

# N, M, K = map(int, input().split())
# solve(N, M, K)


# N, M, K = map(int, input().split())

# '''
# 2 , 2 
# aazz : a가 2개 앞
# azaz azza : a가 1개 앞
# zaaz zaza zzaa : a가 0개 앞
# '''

# def pectorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # for i in range(N + 1):
# #     print(dp[i])
# # print()


# def solve(N, M, K):
#     if (N == 0 or M == 0) and K == 1:
#         if M == 0:
#             print("a" * N)
#             return
#         else:
#             print("z" * M)
#             return

#     maxSize = pectorial(N + M) / (pectorial(N) * pectorial(M))
#     if K > maxSize:
#         print(-1)
#         return

#     dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

#     for r in range(1, N + 1):
#         dp[r][0] = 1

#     for c in range(1, M + 1):
#         dp[0][c] = 1

#     for r in range(1, N + 1):
#         for c in range(1, M + 1):
#             dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

#     r, c = N, M
#     ans = ""
#     while r > 0 and c > 0:
#         startFromA = dp[r][c - 1]
#         # print(f"r: {r} c: {c} startFromA: {startFromA}, K: {K}")
#         if K <= startFromA:
#             c -= 1
#             ans += "a"
#         else:
#             K -= dp[r][c - 1]
#             r -= 1
#             ans += "z"

#     if r == 0:
#         while c > 0:
#             c -= 1
#             ans += "a"
#     else:
#         while r > 0:
#             r -= 1
#             ans += "z"

#     print(ans)

# #solve(K)

# solve(100, 0, 1)




