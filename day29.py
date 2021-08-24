import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 자료 구조 = stack
    : String을 그대로 사용하거나 Array를 사용하면 수정/삭제가 잦아서 시간복잡도 문제가 생긴다.
    : 커서를 기준으로 좌우로 나누어서 stack 2개에 저장하면 될 것 같다.
    : dequeue가 아니라 stack을 사용하는 이유는 문자열을 컨트롤할 때는
        : 한번에 커서 전후의 data 하나씩만 조작가능하기 때문에 data가 들어오고 나가는 출입구는 하나면 된다.

# 문제 풀이 아이디어
    : 커서 좌우를 담당하는 stack을 만들어서
    : 입력에 맞게 문자열을 조작하고
    : 마지막에 합쳐서 출력한다.

# 의사코드
1. stack 2개를 선언한다.
2. 입력을 받는다.
3. 입력된 문자열을 반복문을 돌면서
    3-1. 문자가 입력되면 왼쪽 stack에 넣는다.
    3-2. 커서가 왼쪽으로 이동하면 왼쪽 stack에서 빼서 오른쪽에 넣는다.
    3-3. 커서가 오른쪽으로 이동하면 오른쪽에서 왼쪽으로 넣는다.
    3-4. 백스페이스가 들어오면 왼쪽 스택에서 pop한다.
4. stack에 남아있는 결과물을 출력한다.
    4-1. 왼쪽 스택은 pop된 순서의 역순으로
    4-2. 오른쪽 스택은 pop된 순서대로 출력한다.
'''
n = int(input())
for _ in range(n):
    commands = input()
    left = []
    right = []
    for command in commands:
        if command == "-":
            if left:
                left.pop()
        elif command == "<":
            if left:
                right.append(left.pop())
        elif command == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(command)
    right.reverse()
    result = left + right
    print(''.join(result))


'''
# 사용해야 하는 자료 구조 = heap
    : 가장 작은 카드묶음부터 비교해야 최소한으로 비교할 수 있다.
    : 최소 힙을 사용하면 된다.

# 문제 풀이 아이디어
    : 총 n - 1 비교를 하는데
    : 가장 작은 두 개의 카드뭉치는 n - 1번 비교하고
    : 세 번째로 작은 카드뭉치부터는 n - cnt - 1번 비교한다.

# 의사코드
    1. 입력을 받는대로 최소 heap에 넣는다.
    2. cnt = 1로 설정한다.
    3. pop 2번한 것을 더하고 n - cnt을 곱한다.
    4. while heap: 반복문을 돌면서
        4-1. cnt += 1하고
        4-2. pop한 것 곱하기 n - cnt해서 이전 합에 더한다.
    5. 결과를 출력한다.
'''

'''
# 사용해야 하는 자료구조 = heap
    : 매번 비교할 때마다 카드 뭉치 중에서 가장 작은 것 2개를 뽑아야 한다.
    : 최소 힙 사용

# 문제 풀이 아이디어
    : 총 n - 1번 비교를 하는데 그 때마다 가장 작은 뭉치 2개를 비교
    : 비교해서 만들어진 카드 뭉치를 다시 힙에 넣어야 한다.

# 의사코드
    1. 입력을 받아서 최소 heap에 넣는다.
    2. result = 0으로 선언한다.
    3. 최소 heap에서 2개를 뽑아서 더한 값을
        3-1. result에 더하고
        3-2. heap에 넣는다.
    4. heap의 길이가 1이면 result를 출력한다.

# 시간복잡도
    : heap에 넣고 빼는 것이 O(logn)
    : n - 1 번 반복된다.
    : 최종적으로 O(nlogn)
'''
# import sys
# import heapq
# hq = []
# n = int(input())
# for _ in range(n):
#     heapq.heappush(hq, int(sys.stdin.readline()))
# result = 0
# while len(hq) > 1:
#     current = heapq.heappop(hq) + heapq.heappop(hq)
#     result += current
#     heapq.heappush(hq, current)
# print(result)

'''
# 사용해야 하는 자료구조 = heap, deque
    : 어떤 수열이 들어올지 모르니까 중앙값을 구하는 규칙성을 찾을 수는 없다.
    : 따라서 중앙값을 구하려면 수열이 들어올 때마다 정렬을 해야하는데
    : 그런 상황에서 가장 시간복잡도가 낮은 자료구조가 힙이다.

    : 수열을 저장하고 하나하나 힙에 넣기 위해서 deque를 사용한다.
        : Array를 사용하면 pop(0)가 시간복잡도가 O(n)이라 오래 걸린다.

# 문제 풀이 아이디어
    : heap을 선언해서 수열을 순서대로 넣고
    : 홀수인 n번째가 들어갈 때 마다 n // 2 + 1까지 빼서 출력한다.

# 의사코드
    1. 입력을 받고 heap을 선언한다.
    2. m // 10 + 1만큼 반복문을 돌면서 수열을 전부 deque에 저장한다.
    3. 첫줄에는 m // 2 + 1을 출력한다.
    4. deque에서 heap을 넣는데 넣을 때 마다 cnt를 센다.
        4-1. cnt가 홀수일 때 cnt // 2 만큼빼고 하나 더 뺀 것을 출력한다.
        4-2. 그리고 다시 넣는다.
    5. cnt % 20 == 19일 때마다 줄바꿈을 한다.

# 시간복잡도
    : heap은 삽입/삭제가 O(logn)
    : 중간값을 구하는 과정에서 삽입/삭제가 많이 일어나는데 O(n) ~ O(n**2)가 아닐까 싶다. 

# 블로그 참고
    : 최대 heap하나와 최소 heap하나를 두고 두 heap의 길이를 동일하게 유지하면서
    : 중앙값을 찾는 방법이 더 시간복잡도가 낮아 보인다 (삽입/삭제를 덜 실시함.)
'''
# import heapq
# from collections import deque

# t = int(input())

# for _ in range(t):
#     m = int(input())
#     print(m // 2 + 1)
#     dq = []
#     for _ in range(m // 10 + 1):
#         dq += list(map(int, input().split()))
#     dq = deque(dq)
#     cnt = 0
#     hq = []
#     while cnt < m:
#         heapq.heappush(hq, dq.popleft())
#         cnt += 1
#         if cnt % 2 == 1:
#             interim = []
#             for _ in range(cnt // 2):
#                 interim.append(heapq.heappop(hq))
#             median = heapq.heappop(hq)
#             print(median, end=" ")
#             interim.append(median)
#             for num in interim:
#                 heapq.heappush(hq, num)
#         if cnt % 20 == 19:
#             print()
#     print()
    