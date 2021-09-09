import sys
sys.stdin=open("input.txt", "r")

N = int(input())
cardPool = list(map(int, input().split()))
M = int(input())
ownCards = list(map(int, input().split()))

cardPool.sort()

def binarySearch(card):
    s = 0
    e = len(cardPool) - 1

    while s <= e:
        m = (s + e) // 2
        if cardPool[m] == card:
            return True
        elif cardPool[m] > card:
            e = m - 1
        else:
            s = m + 1
    
    return False

for card in ownCards:
    if binarySearch(card):
        print(1, end=" ")
    else:
        print(0, end=" ")

# N = int(input())
# budgets = list(map(int, input().split()))
# M = int(input())

# def getAllowedBudget(budget, limit):
#     if budget < limit:
#         return budget
#     else:
#         return limit

# def getTotalCost(limit):
#     result = 0
#     for budget in budgets:
#         result += getAllowedBudget(budget, limit)
#     return result

# s = 1
# e = max(budgets)
# ans = 0

# while s <= e:
#     mid = (s + e) // 2
#     result = getTotalCost(mid)
#     #print(f"s={s}, e={e}, mid={mid}, result = {result}, M = {M}")
#     if result > M:
#         e = mid - 1
#     elif result < M:
#         ans = max(ans, mid)
#         s = mid + 1
#     else:
#         ans = max(ans, mid) # 이부분 빼먹어 계속 틀림
#         break

# print(ans)