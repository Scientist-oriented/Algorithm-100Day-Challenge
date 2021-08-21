import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 자료 구조 = stack
    : 두 쌍이 짝지어지는 문제 = 괄호문제와 유사하다!

# 문제 풀이 아이디어
    : 괄호문제와 동일하게 stack을 사용하면 되는데
    : 열리는 괄호, 닫히는 괄호 구분이 없으므로 바로 전에 stack[-1]과 대조한다.
    : 좋은 단어의 유형
        : AABB -> 좋은 단어끼리 붙어있는 경우
        : ABBA -> 좋은 단어 사이에 좋은 단어가 끼어 있는 경우
        : -> 두 유형 모두 다 위의 stack 아이디어로 검사할 수 있다.

# 의사코드
    1. 문자열을 반복문을 돌면서 (함수로 구현)
        1-1. stack이 비었거나 stack[-1]이 현재 문자와 다르면 append
        1-2. stack[-1]이 현재 문자와 같으면 pop
    2. 최종적으로 stack이 비었으면 True, 아니면 False를 반환
    3. 테스트 케이스 만큼 반복문 돌면서 위 함수에 케이스입력하고 True일 때 cnt++
    4. 결과 출력

# 시간 복잡도
    : 함수 내부의 시간 복잡도가 단어의 길이만큼이고
    : 단어 n개만큼 반복된다. O(단어길이 * n)
    : 다만 단어길이가 1,000,000이하라고 했으므로 
    : n < 1,000,000 일때 O(n)이라고 볼 수 있다.

'''
def isGoodWord(w):
    stack = []
    for c in w:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    if stack:
        return False
    else:
        return True

n = int(input())
cnt = 0
for _ in range(n):
    if isGoodWord(input()):
        cnt += 1
print(cnt)
'''
# 사용해야 하는 자료 구조 = stack
    : 괄호 문제랑 마찬가지로 2세트를 짝 짓는 문제이다.

# 힌트 
   : A, B 선택지가 n개가 아니라 2개 = stack 2사용

# 문제 풀이 아이디어
    : 스택은 2개 사용한다
    : AA가 두개 모여서 아치를 이룰 때
        : B에 스택에 B가 남아 있을 때 
            : BAAB 는 가능
            : ABAB 는 불가능 -> 두 경우만 구분하면 될 것 같다.

# 의사코드
    1. 입력을 받고 테스트 케이스의 수만큼 반복문 돌린다.
    2. 문자열을 반복문을 돌면서 (함수로 구현)
        2-1. A와 B를 만날 때 마다 stack이 비면 넣고
        2-2. stack에 있으면 빼는데 반대편 stack이 비어있지 않으면 분기문 실행
            2-2-1. A를 뺄 때 바로 이전 문자가 B였으면 False
            2-2-2. 바로 이전 문자가 A였으면 Continue
        2-3. 최종적으로 OK된 문자열만 True
    3. True가 나온 문자열만 세고 출력
'''
# def isGoodWord(w):
#     stack1 = []
#     stack2 = []
#     for i in range(len(w)):
#         if w[i] == "A":
#             if not stack1:
#                 stack1.append("A")
#             else:
#                 if stack2 and w[i - 1] == "B":
#                     return False
#                 else:
#                     stack1.pop()
#         else:
#             if not stack2:
#                 stack2.append("B")
#             else:
#                 if stack1 and w[i - 1] == "A":
#                     return False
#                 else:
#                     stack2.pop()
#     if stack1 or stack2:
#         return False
#     else:
#         return True


# n = int(input())
# cnt = 0
# for _ in range(n):
#     w = input()
#     if isGoodWord(w):
#         cnt += 1
# print(cnt)

'''
# 사용해야 하는 자료 구조: stack
    : 각 음마다 스택을 사용해서 총 6개 사용한다.
    
# 문제 풀이 아이디어
    : 프렛을 짚을 때마다 stack에 프렛 번호를 넣는다.
    : stack의 제일 위와 짚으려는 프렛을 비교해가면서 하면 될 것 같다.
    : 넣고 뺄 때마다 cnt 추가하기

# 의사 코드
    1. 입력을 받고 배열 1개에 6개 스택을 선언한다.
    2. 반복문으로 음과 프렛을 받으면서 (스택에 추가하거나 빼면 cnt += 1)
        2-1. 해당 음의 stack이 비었거나 누르려는 프렛이 stack[-1] 프렛이 작으면 stack에 프렛 추가
        2-2. 해당 음의 stack[-1] 프렛이 누르려는 프렛과 같으면 pass
        2-3. 해당 음의 누르려는 프렛이 더 작으면 stack[-1]이 누르려는 프렛보다 작아질 때까지 stack.pop()
    3. cnt 출력한다.

# 시간 복잡도
    : n만큼 반복되는 반복문 1개
    : 내부에 while문이 있기는 한데 n보다 한참 작을 것으로 생각된다.
    : O(n)보다 살짝 큰 정도?

'''
# n, prett = map(int, input().split())
# stack = [[] for _ in range(6)]
# cnt = 0
# for _ in range(n):
#     i, p = map(int, input().split())
#     i = i - 1
#     if not stack[i] or stack[i][-1] < p:
#         stack[i].append(p)
#         cnt += 1
#     elif stack[i][-1] == p:
#         continue
#     else:
#         while stack[i] and stack[i][-1] > p:
#             stack[i].pop()
#             cnt += 1
#         if stack[i] and stack[i][-1] == p:
#             continue
#         else:
#             stack[i].append(p)
#             cnt += 1
#     # print(f"p: {p} cnt: {cnt}, stack: {stack}")

# print(cnt)



'''
# 사용해야 하는 자료구조 = deque
    : 기둥들을 자료구조에 순서대로 두고
    : 왼쪽에서 천장까지, 오른쪽에서 천장까지 접근해야 함!
    : 좌우에서 자료를 뺄 수 있는 deque가 적합

# 문제 풀이 아이디어
    : 기둥을 넣고 왼쪽에 오는 순으로 정렬하고
    : 왼쪽에서 천장까지, 오른쪽에서 천장까지 접근하면서 면적 구하면 된다.

# 의사 코드
    1. 입력 받고 왼쪽에 오는 순서대로 정렬하고 천장을 구한다
    2. 먼저 왼쪽에서 반복문을 돌면서 면적을 구한다.
        2-1. 천장을 만나면 멈춘다.
    3. 다음으로 오른쪽에서 반복문을 돌면서 면적을 구한다.
        3-1. 천장을 만나면 멈춘다.
    4. 면적을 합쳐서 출력한다.

# 시간 복잡도
    : 왼쪽, 오른쪽 반복문을 합쳐서 O(n)
    : 기둥 정렬이 O(nlogn)
    : 결과적으로 O(nlogn)
'''
# from collections import deque
# n = int(input())
# polls = list()
# for _ in range(n):
#     l, h = map(int, input().split())
#     polls.append((l, h))
# ceiling = max(polls, key=lambda x: x[1])
# dq = deque(sorted(polls))
# result = ceiling[1] 
# currentPoll = dq.popleft()

# while currentPoll != ceiling:
#     while currentPoll[1] > dq[0][1]:
#         dq.popleft()
#     result += (dq[0][0] - currentPoll[0]) * currentPoll[1]
#     currentPoll = dq.popleft()

# dq.appendleft(currentPoll)
# currentPoll = dq.pop()
# while currentPoll != ceiling:
#     while currentPoll[1] > dq[-1][1]:
#         dq.pop()
#     result += (currentPoll[0] - dq[-1][0]) * currentPoll[1]
#     currentPoll = dq.pop()

# print(result)
    




'''
# 1st, 2nd try에 실패한 이유
    : 처음에는 Array를 써서 이중반복문을 썼는데
        : O(n**2)라서 시간초과가 났다.
    : 두번째는 Array를 역으로 반복하면서
    : 가장 큰수를 저장하면서 구했는데
        : 가장 왼쪽에 있는 수가 아니라 그냥 왼쪽에 있는 수 중에 가장 큰 수를 구하게 됨.

# 결국 블로그 찾아보기 = stack을 써야한다고 한다!
    : 초점를 오큰수를 구하는 수 a[i]에 두고
        : 뒤에 오는 어떤 수가 NGE가 될 수 있는지 구하는 것이 아니라
    : NGE(i)에 초점을 두는 것이다.
        : -> 현재 a[i]가 어떤 수의 NGE가 될 수 있는지 찾는다.

# 문제 풀이 아이디어
    : 아직 NGE를 구하지 못한 수를 stack에 넣어둔다.
    : 그리고 a[1]부터 순회하면서 
        : stack에 있는 index가 a[i]를 NGE로 가질 수 있는지 따진다.
            : stack에 있는 index는 아직 오른쪽에 자기 보다 큰 수를 만나지 못한 수
        : stack이 비었거나 stack[-1]이 a[i]보다 작다면
            : (= stack에는 a[i]보다 큰 수만 들어있다 = a[i]가 더 이상 아래 수들의 NGE가 될 수 없다.)
                : i를 스택에 넣는다.

# 의사코드
    1. 입력을 받는다
    2. 0이 들어 있는 스택과 [-1]이 n개 있는 result를 선언한다.
    3. i < n 동안 반복문을 돌면서
        3-1. stack에 있는 인덱스의 수가 a[i]보다 크면 result에 NGE로 저장
        3-2. stack에 더이상 수가 없거나 a[i]보다 작으면 i를 스택에 넣는다.
    4. 결과를 출력한다.

# 시간 복잡도
    : 반복문 O(n)짜리가 두개 돌아가는 구조인 것 같다.
    : O(n)으로 예상된다.

'''
# n = int(input())
# a = list(map(int, input().split()))
# stack = [0]
# result = [-1 for _ in range(n)]
# i = 1
# while i < n:
#     while stack and a[i] > a[stack[-1]]:
#         result[stack.pop()] = a[i]
#     stack.append(i)
#     i += 1
# result = map(str, result)
# print(' '.join(result))

'''
# 써야할 자료 구조 = Array
    : 수열 이므로 순서를 저장할 수 있어야 한다.
    : 입력은 한번하면 끝이다.
    : 탐색이 잦으므로 탐색이 O(1)인 자료구조를 택한다.

# 문제 풀이 아이디어 (실패)
    : 배열에 저장하고
    : 각 수의 오른쪽을 탐색하면서 큰수를 만나면
    : 출력하면 될 것 같다.

# 의사코드 (실패)
    1. 입력을 받아서 배열에 저장한다
    2. 배열의 반복문을 돌면서
        2-1. 오른쪽 수 부터 탐색하고
        2-2. 작은 것 나오면 바로 프린트
        2-3. 반복문 끝까지 돌면 -1 프린트
# 시간복잡도 (실패)
    : O(n**2)이다...
    : 결국 시간초과 나왔다.

# 새로운 문제풀이 아이디어
    : 결국 이중 반복문을 돌리면 안된다!!
    : 그럼 최댓값을 저장해가면서 하면 어떨까?
    : 배열을 역순으로 돌면서 최댓값을 변수에 저장하고
    : 현재 값과 비교해가면서 출력하면 될 것 같다.

# 새로운 의사 코드
    1. 입력을 받아 배열에 저장한다.
    2. maxNum을 0으로 하고 배열을 거꾸로 돈다.
        2-1. 수가 maxNum보다 작으면 maxNum을 배열에 넣고
        2-2. 수가 maxNum보다 크거나 같으면 배열에 -1 넣고 maxNum 갱신한다.
    3. 배열을 거꾸로 뒤집고 출력한다.
'''
# n = int(input())
# a = list(map(int, input().split()))
# maxNum = 0
# result = []
# for i in range(n - 1, -1, -1):
#     if a[i] < maxNum:
#         result.append(maxNum)
#     else:
#         result.append(-1)
#         maxNum = a[i]
# for num in reversed(result):
#     print(num)


# n = int(input())
# a = list(map(int, input().split()))
# for i in range(n):
#     end = False
#     for j in range(i + 1, n):
#         if a[i] < a[j]:
#             print(a[j], end=' ')
#             end = True
#             break
#     if end:
#         continue
#     print(-1, end=" ")

'''
# 써야할 자료 구조 = stack
    : 괄호가 쌍을 이뤄서 레이저 혹은 쇠막대기를 이루고 있으므로
    : stack을 사용해서 괄호를 열 때 스택에 넣고 닫을 때 빼서
    : 각각 레이저와 막대기를 구분하며 될 것 같다.

# 문제 풀이 아이디어
    : 받은 문자열을 반복문을 돌면서
    : 여는 괄호에 스택에 현재 위치를 (= i) 넣는다.
    : 닫는 괄호에 스택에서 빼는데
        : 각각 조건에 맞게 레이저와 쇠막대기를 구분해서 각각의 배열에 저장
    : 그리고 쇠막대기가 얼마나 잘리는지 계산

# 의사코드
    1. 입력을 받는다
    2. 쇠막대기와 레이저를 저장한 빈 배열을 선언한다.
    3. 입력의 길이 만큼 반복문을 도는데
        3-1. 여는 괄호가 나오면 스택에 i를 넣고
        3-2. 닫는 괄호가 나오면 스택에서 i를 빼서
            3-2-1. 스택에서 나온 수가 i-1이면 레이저에 i - 0.5 저장하고
            3-2-2. 아니면 (stack.pop(), i)로 저장한다.
    4. 쇠막대기 반복문을 돌면서 
        4-1. 쇠막대기 범위에 범위에 레이저가 몇개 들어오는지 체크한다.
    5. 결과를 출력한다.

# 시간 복잡도
    : 처음 나오는 반복문은 O(n)
    : 두번째 나오는 이중 반복문은 O((n/2)**2)로 O(n**2)이라서
    : n 값이 살짝 아슬아슬하기는한데 실제로는 1/4하기 때문에 무난히 될 것으로 예상한다.
'''
# s = input()
# stack = []
# rods = []
# lasers = []
# for i in range(len(s)):
#     if s[i] == "(":
#         stack.append(i)
#     else:
#         if stack[-1] == i - 1:
#             stack.pop()
#             lasers.append(i - 0.5)
#         else:
#             rods.append((stack.pop(), i))
# cnt = 0
# for rod in rods:
#     rod_cnt = 1
#     for laser in lasers:
#         if laser > rod[0] and laser < rod[1]:
#             rod_cnt += 1
#     cnt += rod_cnt
# print(cnt)

'''
# 써야할 자료구조 = set
    : 두 명단을 받아서 겹치는 것을 구하는 문제
    : 교집합 연산을 활용하면 된다.

# 문제 풀이 아이디어
    : 듣도 못한 집합 하나, 보도 못한 집합 하나를 선언해서
    : 교집합을 구한다.
    : 정렬해야 하므로 리스트로 변경한 후 정렬해서 출력한다.

# 의사코드
    1. 첫줄 인풋을 받고 빈 집합 2개 선언
    2. n과 m만큼 반복문을 돌면서 두개의 집합에 넣는다.
    3. 두 집합의 교집합을 구한다.
    4. 리스트로 바꿔서 정렬하고 출력한다.

# 시간복잡도
    : 반복문 n과 m번 두개 니까 O(2n) = O(n)
        : 집합에 삽입은 O(1)
    : 교집합은 O(len(s1) + len(s2))라고 한다
        : 정리하면 결국 O(n)
    : 파이썬의 리스트 정렬은 O(nlogn)
    : 최종적으로 O(nlogn)으로 생각됨
    : n이 500,000이니까 충분하다고 생각됨
'''
# import sys
# n, m = map(int, input().split())
# s1 = set()
# s2 = set()
# for _ in range(n):
#     s1.add(sys.stdin.readline().rstrip())
# for _ in range(m):
#     s2.add(sys.stdin.readline().rstrip())

# s3 = sorted(list(s1.intersection(s2)))

# print(len(s3))
# for name in s3:
#     print(name)

