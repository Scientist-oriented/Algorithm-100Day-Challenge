import sys
sys.stdin=open("input.txt", "r")


'''
# 이취코 p.315 볼링공 고르기 정답코드
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)

# 이취코 p.315 볼링공 고르기 내코드
n, m = map(int, input().split())
balls = list(map(int, input().split()))
count = 0

for i in range(0, len(balls) - 1):
    for j in range(i + 1, len(balls)):
        if balls[i] != balls[j]:
            count += 1

print(count)

# 이취코 p.314 만들 수 없는 금액 답코드
n = int(input())
data = list(map(int, input().split())
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

# 이취코 p.314 만들 수 없는 금액 내코드
n = int(input())
coins = list(map(int, input().split()))
coins.sort()
total = coins[0]
if coins[0] != 1:
    print(1)
    exit()

for i in range(1, len(coins)):
    if coins[i] > total:
        break
    else:
        total += coins[i]

print(total + 1)

# 이취코 p.313 문자열 뒤집기 답코드
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

# 이취코 p.313 문자열 뒤집기 내코드
data = input()
result = 0

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        result += 1

result = (result + 1) // 2
print(result)

# 이취코 p.312 곱하기 혹은 더하기 내코드
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


# 이취코 p.312 곱하기 혹은 더하기 내코드
nums = list(map(int, input()))
result = 1
for num in nums:
    if num <= 1:
        result += num
    else:
        result *= num

if nums[0] == 1:
    print(result - 1)
else:
    print(result)

# 이취코 p.311 모험가 길드 답코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# 이취코 p.311 모험가 길드 내코드

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
count = 0
group = list()

while arr:
    man = arr.pop()
    group.append(man)
    if max(group) == len(group):
        count += 1
        group = list()
    else:
        continue

print(count)
'''            