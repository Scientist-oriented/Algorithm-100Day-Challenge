import sys
sys.stdin=open("input.txt", "r")




"""
# 백준 2437 저울
# 내 첫 코드
n = int(input())
weights = list(map(int, input().split()))

weights.sort(reverse=True)

def canMeasure(x, weights):
    for weight in weights:
        if x == weight:
            return True
        elif x > weight:
            x -= weight
        else:
            continue
    return False

count = 1

while canMeasure(count, weights):
    count += 1

print(count)

# 1부터 하나씩 늘려가면서 계산이 가능한지 확인하는 것이었다. -> 사실상 브루탈포스
# 저 함수부분에서만 그리디 알고리즘 쓰면 된다고 생각함.
# 그래서 시간초과가 나왔다 (n이 상당히 커서 저렇게 하면 안됨)

# 정답코드
n = int(input())
weights = list(map(int, input().split()))

weights.sort()

sum = 0

for weight in weights:
    if sum + 1 < weight:
        break
    sum += weight

print(sum + 1)




"""

