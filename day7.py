import sys
sys.stdin=open("input.txt", "r")

# 이진탐색 반복문으로 구현
array = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(binary_search(array, 3, 0, len(array) - 1))
print(binary_search(array, 4, 0, len(array) - 1))

'''
# 이진탐색 리스트 슬라이싱으로 구현
array = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binary_search(array, target):
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
        return binary_search(array[:mid - 1], target)
    else:
        return binary_search(array[mid + 1:], target)

print(binary_search(array, 1))
print(binary_search(array, 3))
print(binary_search(array, 100))



# 이진탐색 구현

array = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

print(binary_search(array, 3, 0, len(array) - 1))
print(binary_search(array, 4, 0, len(array) - 1))


# 이취코 182쪽 두 배열의 원소 교체
n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA = sorted(arrayA)
arrayB = sorted(arrayB, reverse=True)

for i in range(k):
    # 무조건 더 크다는 보장이 없다!
    if arrayA[i] < arrayB[i]:
        arrayA[i] = arrayB[i]
    else:
        break

print(sum(arrayA))



# 이취코 180쪽 성적이 낮은 순서로 학생 출력하기
n = int(input())
array = list()

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key = lambda x: x[1])

for student in array:
    print(student[0], end=' ')




# 이취코 178쪽 위에서 아래로
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for num in array:
    print(num, end=' ')


# 정렬 구현하기
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 파이썬의 특징을 활용한 더 짧은 퀵정렬 구현

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))


# 선택정렬 소스코드
for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

# 삽입정렬 소스코드
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)

# 퀵정렬 소스코드 (직관적인 형태)
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
'''