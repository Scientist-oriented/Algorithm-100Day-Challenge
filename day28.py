import sys
sys.stdin=open("input.txt", "r")
'''
# 사용해야 하는 자료구조 = heap
    : 메모리 제한이 빡빡한 편이다.
    : 데이터를 전부 저장하고 정렬하면 메모리 초과 걸림
    : 최소힙을 활용해서 데이터가 들어올 때마다 가장 큰 것 n개만 저장하면서 가야한다.

# 문제 풀이 아이디어
    : 힙을 만들어서 입력이 들어올 때마다 최소 힙에 넣는다.
    : n개를 빼고 전부 다 pop해 버린다.
    : 마지막에 pop해서 출력한다.

# 의사 코드
    1. n을 입력을 받고 heap을 선언한다.
    2. n만큼 반복문을 돌면서 각줄의 입력을 받아서 힙에 넣고
        2-1. heap의 길이가 n이 될 때까지 pop한다.
    3. 마지막에 pop해서 출력한다.

# 시간복잡도
    : heap은 삽입 삭제가 O(logn)이므로
    : 최종적으로 O(nlogn)

# 공간복잡도
    : 검색결과 heap의 공간복잡도는 O(n)이라고 한다.
'''
import heapq
hq = []
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(hq, num)
        while len(hq) > n:
            heapq.heappop(hq)
print(heapq.heappop(hq))


'''
# 사용해야 하는 자료구조 = queue
    : FIFO 방식을 사용하기 때문에
    : 중요도를 따지는 상황에서 탐색을 사용하기는 하는데
    : 어차피 순차적으로 다 따져야 하기 때문에 O(n)이다 (Array와 동일)

# 문제 풀이 아이디어
    : 큐를 만들고 인쇄물들을 넣는다. (처음에 들어온 순서 기록)
    : 큐에서 나오면 중요도를 확인하고 큐를 돌면서 중요도 확인
        : 가장 높으면 인쇄
        : 높은거 있으면 뒤에 넣기

# 의사코드
    1. t와 n을 입력 받는다.
    2. deque에 인쇄물을 넣는다.
    3. popleft()를 하면서
        3-1. 나머지 문서들 보다 중요도가 높으면 인쇄
            3-1-1. cnt += 1
        3-2. 나머지 문서들 보다 중요도가 낮으면 append()
    4. cnt를 출력한다.

# 시간복잡도
    : 문서들을 돌면서 프린트할 것 찾는게 O(n) (정확히는 n보다 크다)
    : 그 반복문 안에서 다른 문서들과 중요도를 비교하는데 O(n) (정확히 n보다 작다)
    : n이 최대 100이므로 아주 넉넉하게 해결 가능
'''

# from collections import deque

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     prints = list(map(int, input().split()))
#     pages = deque()
#     for i in range(len(prints)):
#         pages.append((i, prints[i]))
#     # pages = deque([(i, prints[i]) for i in range(len(prints))])
#         # ✅ 더 깔끔하게 선언할 수 있다!
#     cnt = 0
#     while pages:
#         isPrinted = True
#         current = pages.popleft()
#         # 🚫 이 반복문 대신에 max를 쓰면 더 간단하다!
#             # 이중 반복문 필요 없음
#         for page in pages:
#             if page[1] > current[1]:
#                 pages.append(current)
#                 isPrinted = False
#                 break
#         if not isPrinted:
#             continue
#         cnt += 1
#         if current[0] == m:
#             print(cnt)
