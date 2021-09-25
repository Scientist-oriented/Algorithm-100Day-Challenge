import sys
sys.stdin=open("input.txt", "r")

# 기타 레슨
# 파라메트릭 서치
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

s = max(lectures)
e = sum(lectures)
ans = 100000

while s <= e:
    mid = (s + e) // 2
    length = 0
    numOfBlue = 1

    for lecture in lectures:
        if length + lecture <= mid:
            length += lecture
        else:
            numOfBlue += 1
            length = lecture

    if numOfBlue <= M:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
    