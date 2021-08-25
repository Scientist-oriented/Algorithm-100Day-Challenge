import sys
sys.stdin=open("input.txt", "r")

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    stack = []
    for char in word:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    if not stack:
        cnt += 1
print(cnt)

# import sys
# import heapq
# n = int(input())
# hq = []
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         heapq.heappush(hq, (abs(num), num))
#     else:
#         if not hq:
#             print(0)
#         else:
#             print(heapq.heappop(hq)[1])

'''
# 써야하는 자료구조 = stack
    : 여는 괄호와 닫는 괄호가 쌍을 이뤄야하는 괄호 문제처럼
    : A 혹은 B가 서로 쌍을 이룰 수 있는지 체크해야 한다.
    : stack을 활용하면 된다.

# 좋은 단어의 유형
    : AABB -> 좋은 단어 2개가 붙어 있는 경우
    : ABBA -> 좋은 단어 사이에 좋은 단어가 있는 경우

    : 두 유형 모두 stack을 활용해서 
        : stack[-1]과 같은 경우 pop해서 좋은 단어를 만들고
        : stack[-1]과 다른 경우 append해서 쌍을 이룰 문자열을 기다려서 풀 수 있다.

# 의사코드
    1. n을 입력 받고 그만큼 반복문을 돌린다.
    2. 정답을 저장한 변수 cnt = 0를 선언한다.
    3. 빈 stack을 선언하고 input을 받은 문자열을 반복문을 돌면서
        3-1. 현재 문자 == stack[-1]이면 pop()
        3-2. 현재 문자 != stack[-1]이면 append()한다.
    4. stack이 비었다면 좋은 문자 cnt += 1한다.
    5. cnt를 출력한다.

# 시간 복잡도
    : 첫 반복문이 O(n)
    : 내부의 두번째 반복문이 O(len(단어))
    : 인데 모든 단어의 합이 1,000,000을 넘지 않으므로 1초 안에 가능
'''
