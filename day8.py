import sys
sys.stdin=open("input.txt", "r")

# 동적프로그래밍을 활용한 피보나치 수열 (재귀함수 활용)
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    else:
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

print(fibo(20))

# 동적프로그래밍을 활용한 피보나치 수열 (반복문 활용)
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

'''
# 이취코 떡볶이 떡 만들기 모범 답안
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while (start <= end):
    mid = (start + end) // 2
    total = 0

    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

# 이취코 p.201 떡볶이 떡 만들기
def find_weight(array, mid):
    weight = 0
    for i in range(mid, len(array)):
        weight += i * array[i]
    return weight


def find_height(target, array, start, end):
    if start >= end:
        return end

    mid = (start + end) // 2

    if find_weight(array, mid) == target:
        return mid
    elif find_weight(array, mid) < target:
        return find_height(target, array, start, mid - 1)
    else:
        return find_height(target, array, mid + 1, end)

n, m = map(int, input().split())
array = map(int, input().split())
cakes = [0] * 2000000001

for cake in array:
    cakes[cake] += 1

result = find_height(m, cakes, 0, 2000000001)
print(result)




# 이취코 p.197 부품찾기 - 집합 자료형으로 풀기
n = int(input())
parts = set(map(int, input().split()))
m = int(input())
wanted_parts = list(map(int, input().split()))

for wanted_part in wanted_parts:
    if wanted_part in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# 이취코 p.197 부품찾기 - 계수정렬로 풀기
n = int(input())
parts = list(map(int, input().split()))
m = int(input())
wanted_parts = list(map(int, input().split()))

parts_count = [0] * 1000001

for part in parts:
    parts_count[part] += 1

for wanted_part in wanted_parts:
    if parts_count[wanted_part] != 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')




# 이취코 p.197 부품찾기 - 이진탐색으로 풀기
n = int(input())
parts = list(map(int, input().split()))
m = int(input())
wanted_parts = list(map(int, input().split()))

parts.sort()

def binary_search(target, array):
    if len(array) == 0:
        return False

    if len(array) == 1:
        if array[0] == target:
            return True
        else:
            return False

    mid = len(array) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(target, array[:mid])
    else:
        return binary_search(target, array[mid + 1:])

for i in range(m):
    wanted_part = wanted_parts[i]
    result = binary_search(wanted_part, parts)
    if result:
        print("yes", end=' ')
    else:
        print("no", end=' ')



# 이취코 p.182 두 배열의 원소 교체

n, k = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

print(sum(arrayA))

# 이취코 p.180 성적이 낮은 순서대로 학생 출력하기
n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, score))

array.sort(key= lambda x: x[1])

for student in array:
    print(student[0], end=' ')

# 이취코 p.178 위에서 아래로
n = int(input())
array = []

for _ in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)

for num in array:
    print(num, end=' ')
'''