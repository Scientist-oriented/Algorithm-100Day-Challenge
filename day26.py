import sys
sys.stdin=open("input.txt", "r")

'''
# 써야할 자료구조 = stack
    : stack을 활용한 문제이다.

# 문제 풀이 아이디어
    : 먼저 가능 vs 불가능을 구분해야 한다.
        : 스택으로 만들다가 안되면 NO 출력하기
    : n을 뽑으려면 1 ~ n까지 일단 넣고 뽑아야 한다.
    : + 뽑을 때는 무조건 내림차순이다.
        : 현재까지 스택에 넣은 값보다 큰 수가 나오면 그 때까지 스택에 넣고 뽑는다.
        : 아니면 스택에서 뽑는데
            : 현재 인풋과 다르면 NO

# 의사코드
    1. 첫줄 인풋을 받는다.
    2. 빈 스택과 결과를 저장하는 문자열을 선언한다.
    3. maxNum으로 지금까지 스택에 들어간 최대 값을 저장한다.
    4. n줄 만큼 반복문을 돌리면서
        4-1. 스택 최대값이 인풋보다 작으면 될 때까지 넣고 마지막에 1번 뺀다.
        4-2. 스택 최대값이 인풋보다 작으면
            4-2-1. 인풋이 스택에서 뽑은 것과 같으면 Continue
            4-2-2. 인풋이 스택에서 뽑은 것과 다르면 NO
    5. 결과를 출력한다.

# 시간복잡도
    : 일단 n 만큼 반복문
    : 추가적으로 내부에 스택에 넣는 과정도 반복문이 쓰인다.
        : 이 반복문은 한번에 n이 아니라 상위 반복문이 돌 동안 통틀어서 n이다. (무시해도 되지 않을까? 혹은 logn?)
    : n이 커서 O(n**2)은 안될 것 같다. 하지만 풀린 것으로 보다 O(n**2)보다는 작다.
'''
n = int(input())
stack = []
result = ""
maxNum = 0
for _ in range(n):
    num = int(input())
    if num > maxNum:
        while num > maxNum:
            maxNum += 1
            stack.append(maxNum)
            result += "+"
        stack.pop()
        result += "-"
    elif num < maxNum:
        if stack[-1] == num:
            stack.pop()
            result += "-"
        else:
            print("NO")
            exit()

for char in result:
    print(char)


'''
# 써야할 자료구조 = stack
    : 후위 표기식은 연산자를 만나면 가장 최근의 숫자 2개를 연산한다.
    : 선입후출의 stack 자료구조의 사용이 적절하다.

# 문제 풀이 아이디어
    : 피연산자는 stack에 넣는다.
    : 연산자를 만나면 stack에 있는 숫자 2개를 빼와서 연산한다

# 의사코드
    1. 첫줄, 둘째줄 인풋을 받는다.
    2. n만큼 피연산자의 값을 저장한다. (아스키코드 활용)
    3. 둘째줄 string을 돌면서 연산한다.
        3-1. 피연산자를 만나면 stack에 넣는다
        3-2. 연산자를 만나면 해당 연산자로 stack에서 두 연산자를 꺼내어 연산한다. (순서 주의)
    4. stack에 마지막에 남은 수 1개를 출력한다.

# 시간 복잡도
    : stack에 넣고 빼는 것은 O(1)
    : string의 길이만큼 O(n)을 가진다.
'''

# n = int(input())스
# string = input()
# operand = [0] * 26
# for i in range(n):
#     operand[i] = int(input())
# stack = []
# for char in string:
#     if char.isalpha():
#         stack.append(operand[ord(char) - ord("A")])
#         continue
#     b = stack.pop()
#     a = stack.pop()
#     if char == "+":
#         stack.append(a + b)
#     elif char == "-":
#         stack.append(a - b)
#     elif char == "*":
#         stack.append(a * b)
#     else:
#         stack.append(a / b)

# print(f"{stack[0]:.2f}")
    

'''
# 써야할 자료구조 = deque
    : 중간에 삽입하고 삭제하는 횟수가 500,000번이 되므로 배열로 하면 시간초과 날 가능성 있음
    : 삽입, 삭제가 빠른 deque를 사용해야 함.

# 문제 풀이 아이디어
    : 커서가 항상 deque 맨앞에 있다고 생각하면
    : L은 pop -> appendleft
    : R은 popleft -> append
    : B는 pop
    : P는 appendleft
    : 문장 맨앞, 맨뒤를 예외처리를 해야함! -> 문장 맨 뒤에 0을 붙인다.

# 의사코드
    1. 인풋을 받아서 deque에 저장한다. deque맨 뒤에 0을 붙인다.
    2. 반복문을 m만큼 돌면서
        2-1. 명령어를 각각 처리한다.
        2-2. 0을 활용해서 예외처리한다.
    3. deque를 맨 뒤에 0이 올 때까지 돌린다.
    4. 양식에 맞게 출력한다.

# 시간복잡도
    : m 만큼 입력을 받는 반복문
    : 그 반복문 내부의 연산들은 모두 O(1)
        : 시작문자인지 확인하려고 dq[0]이나 dq[-1]로 접근하면 오래 걸릴 것 같다. (질문하기)
    : 최종적으로 O(m)
'''
# import sys
# from collections import deque
# sentence = input()
# dq = deque(char for char in sentence)
# dq.appendleft("S")
# m = int(sys.stdin.readline())
# for _ in range(m):
#     command = sys.stdin.readline().rstrip()
#     if command == "L": 
#         char = dq.pop()
#         if char == "S": # 탐색하면 오래걸린다 무조건 pop해서 확인
#             dq.append(char)
#         else:
#             dq.appendleft(char)
#     elif command == "D":
#         char = dq.popleft()
#         if char == "S":
#             dq.appendleft(char)
#         else:
#             dq.append(char)
#     elif command == "B":
#         char = dq.pop()
#         if char == "S":
#             dq.append(char)
#         else:
#             continue
#     else:
#         charToAdd = command[-1]
#         dq.append(charToAdd)

# while True:
#     char = dq.popleft()
#     if char != "S":
#         dq.append(char)
#     else:
#         break

# print(''.join(dq))

'''
# 써야할 자료구조 = deque
    : 요세푸스 문제와 마찬가지로 원의 경우 deque로 푸는 것이 좋음
    : 왼쪽으로 가는 연산의 경우 pop -> appendleft로 구현할 수 있다.

# 문제 풀이 아이디어
    : 풍선의 번호들을 deque로 받는데
    : 풍선의 맨 처음 위치를 기억해야 하니까 (원래 풍선 순서, 쪽지숫자)의 튜플로 받는다.
    : popleft = 풍선 터뜨리기 (일단 터뜨리고 나서 숫자를 센다고 했음)
    : 안에 있는 번호에 맞게 이동
    : dq의 길이가 0일 때까지 반복

# 의사코드
    1. 인풋을 받는다, 두번째 줄은 deque로 변환한다.
    2. while문으로 len(dq) > 0인 동안 반복한다.
        2-1. 일단 popleft해서 터뜨리고 풍선 위치는 빈배열에 저장
        2-2. 쪽지 숫자만큼 반복문 실행
            2-2-1. 양수의 경우 popleft -> append
            2-2-2. 음수의 경우 pop -> appendleft
    3. 배열을 양식에 맞게 출력한다

# 시간복잡도
    : while 반복문이 n번 반복된다.
    : 내부에서 풍선 위치 이동하는게 최대 n번 반복 (dq 연산은 O(1))
    : O(n**2)로 예상된다. n이 1000이므로 시간 내에 풀이가 가능하다.
'''

# from collections import deque
# n = int(input())
# balloons = list(map(int, input().split()))
# balloons = deque((i + 1, balloons[i]) for i in range(len(balloons)))
# result = []
# while len(balloons) > 0:
#     balloon = balloons.popleft()
#     result.append(str(balloon[0])) # str으로 바꿔야지 join 가능!
#     if len(balloons) < 1: # 마지막 1개가 빠져나가면 멈춰야
#         break
#     if balloon[1] > 0:
#         for _ in range(balloon[1] - 1):
#             balloons.append(balloons.popleft())
#     else:
#         for _ in range(-balloon[1]):
#             balloons.appendleft(balloons.pop())

# print(' '.join(result))

'''
# 써야할 자료구조 = deque
    : 원을 나타내는 자료구조는 없으므로 list, deque 등을 사용해서 원을 일자로 펴야함.
    : 한 사람이 제거되면 제거된 사람이 첫 번째 사람이 되어서 k번째 사람을 제거함.
    : 따라서 앞뒤 이동과 삭제가 빈번하게 일어나므로 list 보다는 deque를 사용하는 것이 좋음.

# 문제 풀이 아이디어
    : 1 ~ n의 deque를 만들어 원을 표현한다.
    : k번째 사람을 제거하는 것을 deque의 [0]을 [-1]로 k - 1번 보내고 popleft하는 것으로 구현

# 의사코드
    1. 인풋을 받는다. dq를 1 ~ n의 deque로 만든다.
    2. while문을 사용해서 dq의 길이가 0 보다 큰 동안 실행한다.
        2-1. dq에서 popleft한 것을 append k - 1번 한다
        2-2. 그리고 dq[0]을 빼서 빈 배열에 저장해둔다.
    3. 배열을 양식에 맞게 순서대로 출력한다.

# 시간복잡도
    : while 반복문을 실행하는데 총 n번 실행됨
    : 그 내부에 있는 반복문은 k번 실행됨 (내부의 dq 연산은 O(1))
    : O(n**2)이 예상된다. n이 최대 5000이므로 시간 내에 해결이 가능하다.
'''
# from collections import deque
# n, k = map(int, input().split())
# dq = deque(i for i in range(1, n + 1))
# result = []
# while len(dq) > 0:
#     for _ in range(k - 1):
#         dq.append(dq.popleft())
#     result.append(str(dq.popleft()))
# print("<"+', '.join(result)+">")
'''
# 써야할 자료구조 = deque
    : 일단 맨 앞에서 원소를 뽑아내야 하므로 선입후출 방식을 큐를 써야함
    : 추가적으로 왼쪽 이동, 오른쪽 이동 연산도 원소를 뽑아내고 앞에 넣거나 뒤에 넣은 것임.
    : 세 가지 연산을 모두 O(1)로 할 수 있는 deque자료구조를 사용함.

# 문제풀이 아이디어
    1. 먼저 뽑아낼 수 있는 원소는 0번째 인덱스이므로 0번째 인덱스로 원하는 수를 보내야 한다.
    2. 왼쪽 한칸 vs 오른쪽 한칸 연산 중에 더 빠른 연산을 골라서 해야 한다.
    3. 큐의 현재 상태를 저장해야 한다.

# 의사코드
    1. 인풋을 받는다, 두 번째 줄은 배열로 저장한다.
    2. 1 ~ n까지 deque를 선언한다.
    3. 배열에서 하나씩 빼서 반복문을 돌린다.
        3 - 1. 왼쪽 한칸 vs 오른쪽 한칸 중에 더 적게 필요한 것을 고른다.
            : 현재 목표 k의 인덱스 번호 vs len(큐) - 현재 인덱스 중에 작은 것
        3 - 2. 반복문으로 연산을 실제로 실시하고 연산 횟수는 cnt에 저장한다.
    4. cnt를 출력한다.

# 시간 복잡도
    : 먼저 M 으로 반복문 1개
    : 그 안에서 큐의 연산을 실제로 수행하는 반복문 1개로 (내부의 dq 연산은 O(1))
    : O(n**2)이 예상된다. n은 최대 50이므로 시간 내에 해결이 가능하다.
'''
# from collections import deque
# n, m = map(int, input().split())
# nums = list(map(int, input().split()))

# dq = deque(i for i in range(1, n + 1))

# cnt = 0
# for k in nums:
#     index = dq.index(k)
#     if index <= len(dq) - index:
#         for _ in range(index):
#             dq.append(dq.popleft())
#         dq.popleft()
#         cnt += index
#     else:
#         for _ in range(len(dq) - index):
#             dq.appendleft(dq.pop())
#         cnt += len(dq) - index 
#             # 먼저 더하고 pop해야 함!!!
#         dq.popleft()        
# print(cnt)


