# import sys
# sys.stdin=open("input.txt", "r")

# 이취코 p.323 문자열 압축 답코드
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j: j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

a = "apple"
print(a[3:100])
print(len(a[3:100]))

'''
# 이취코 p.323 문자열 압축 내코드 -> 결국 안됨
def solution(s):
    length = len(s)
    for i in range(1, len(s) // 2 + 1):
        result = []
        start = 0
        end = i
        temp = []
        while end >= (len(s) - 1):
            num = 1
            while s[start : end] == s[start + i : end + i]:
                num += 1
                start = start + i
                end = end + i
                print(start, end)
            if num > 1:
                temp.append(str(num))
                temp.append(s[start:end])
            else:
                temp.append(s[start:start+1])
                start += 1
                end += 1
        zipped = ''.join(temp)
        result.append(len(zipped))
    return min(result)

print(solution("aabbaccc"))

# 이취코 p.322 문자열 재정렬 답코드
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))


# 이취코 p.321 럭키스트레이트 답코드
 n = input()
 length = len(n)
 summary = 0

 for i in range(length // 2):
     summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")


# 이취코 p.321 럭키스트레이트 내코드
arr = list(map(int, input()))
half = len(arr) // 2

first_half = arr[:half]
second_half = arr[half:]

if sum(first_half) == sum(second_half):
    print("LUCKY")
else:
    print("READY")

# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891
'''