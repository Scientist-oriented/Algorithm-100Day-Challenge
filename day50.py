# 뱀
'''
# 자료구조/알고리즘
    : 구현
# 풀이 방법
    1. N * N의 이차원 배열에 사과를 입력한다.
    2. 현재 뱀의 위치를 기준으로 방향전환 시점 이전까지의 이동을 구현한다.
        : 사과를 먹으면 뱀의 길이를 증가시킨다.
        : 뱀 머리 이동 -> 사과 섭취 or 꼬리 비우기를 하나의 함수로 구현한다.
    3. 뱀의 머리가 이차원 배열을 벗어나거나 뱀의 위치 (자기 자신의 몸)과 부딪히면 몇초가 지났는지 출력한다.
'''
# 게리맨더링 2
'''
# 자료구조/알고리즘
    : 완전탐색
# 풀이방법
    1. 가능한 모든 x, y와 d1, d2에 대해서 모든 가능한 선거구를 만든다.
    2. 각 선거구 마다 인구수를 구하면서 최댓값과 최솟값의 차이를 구한다.
    3. 그 차이 중에 최솟값을 출력한다.
'''
# 고스택
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 각 연산을 함수로 구현한다.
    2. 명령어를 배열에 저장해 프로그램을 만든다.
    3. stack에 입력 값을 넣고 프로그램의 명령어를 돌면서 stack을 만든다.
    4. 스택에 저장된 값에 맞게 답을 출력한다.
'''
# 괄호 제거
'''
# 자료구조/알고리즘
    : stack
# 풀이방법
    1. 식을 index 순서대로 탐색하면서 stack을 활용해 괄호의 쌍을 찾는다.
        : 여는 괄호가 나오면 stack에 index를 넣고
        : 닫는 괄호가 나오면 stack에서 index를 pop해서 닫는 괄호의 index와 함께 저장한다.
    2. 1에서 얻은 괄호쌍을 바탕으로 괄호쌍이 생략된 식을 만든다.
    3. 사전 순대로 정렬해서 출력한다.
'''
# 색종이
'''
# 자료구조/알고리즘
    : 완전 탐색
# 풀이방법
    1. 100 * 100 이차원 배열을 만든다.
    2. 색종이의 위치를 기반으로 색종이가 붙여진 영역을 표시한다.
    3. 완전탐색으로 색종이가 붙여진 영역을 모두 탐색한다.
'''
# 괄호의 값
'''
# 자료구조/알고리즘
    : stack
# 풀이방법
    1. 입력을 탐색하면서 열린 괄호는 stack에 넣고 닫힌 괄호는 stack에서 pop한다.
    2. 연산의 결과도 stack에 push한다.
    3. 닫힌 괄호에서 pop한 결과가 숫자라면 같은 모양의 열린 괄호가 나올 때까지 pop하고
        : 그 때까지 나온 숫자를 모두 더해서 곱셈을 해서 push한다.
    4. 입력 탐색이 끝나면 stack에 남은 수를 모두 더해서 출력한다.
'''
# 과제
'''
# 자료구조/알고리즘
    : 정렬
# 풀이방법
    1. 과제를 마감일이 늦은 순 -> 점수가 높은 순으로 정렬해서
    2. 가장 마지막 마감일부터 역순으로 할 수 있는 과제의 점수를 더한다. 
''' 

# 팰린드롬 만들기
'''
# 자료구조/알고리즘
    : Array
# 풀이방법
    1-1. 문자열의 길이가 짝수인 경우 모든 알파벳이 짝수개 있는지 확인한다.
    1-2. [0] * 26을 활용해서 알파벳의 갯수를 센 후 해당 알파벳들의 갯수를 1/2해서 배열에 넣는다.
    1-3. 정렬한후 팰린드롬으로 바꾸어 출력한다.
    2-1. 문자열의 길이가 홀수인 경우는 모든 알파벳이 짝수개이고 1개만 홀수개인지 확인한다.
    2-2. 동일하게 알파벳 갯수를 센 후 해당 알파벳을 팰린드롬으로 바꾸어 출력한다.
'''
# 제로
'''
# 자료구조/알고리즘
    : stack
# 풀이방법
    1. 입력이 0이 아닌 정수가 들어오면 stack에 push하고
    2. 0이 들어오면 stack에서 pop한다.
    3. 마지막에 stack에 남은 수를 합한다.
'''
# 2048 (Easy)
'''
# 자료구조/알고리즘
    : dfs
# 풀이방법
    1. dfs를 통해서 상하좌우로 5번 이동하는 모든 경우를 탐색한다.
    2. 각 방향으로 이동한 다음에 같은 수가 이동한 방향으로 인접해있다면 합친다.
    3. 5번 탐색하면 가장 큰 블록을 찾아서 최댓값을 갱신한다.
'''
# AC
'''
# 자료구조/알고리즘
    : deque
# 풀이방법
    1. list는 뒤집는게 오래 걸리니까 deque를 사용한다.
    2. 정방향인지 역방향인지 R이 나올 때마다 바꾼다.
    3. 정방향이면 D가 나왔을 때 앞에서 빼고, 역방향이면 뒤에서 뺀다.
    4. 결과를 출력한다.
'''
# 미세먼지 안녕!
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 이차원 배열을 만들어 입력을 받는다.
    2. 배열을 완전탐색하면서 먼지를 만나면 확산한다.
    3. 공기청정기의 위치에 따라서 바람의 순환을 계산한다. 
'''
# 센서
'''
# 자료구조/알고리즘
    : 그리디
# 풀이방법
    1. 센서들의 위치를 정렬한다.
    2. 센서들 사이의 길이를 저장하는 배열을 만들어서 i ~ i + 1센서의 거리를 arr[i]에 저장한다.
    3. 센서들 사이의 길이 중에서 가장 큰 순서대로 k - 1개를 제거한다.
    4. 센서들 사이의 길이의 합을 출력한다.
'''
# 시험 감독
'''
# 자료구조/알고리즘
    : 그리디
# 풀이방법
    1. 각 시험장의 응시자 수를 배열로 저장한다.
    2. 각 시험장을 탐색하면서 (응시자수 - 총감독관감시인원) // (부감독관감시인원) + 1을 result에 더해나간다.
'''
# 도키도키 간식드리미 
'''
# 자료구조/알고리즘
    : stack, queue
# 풀이방법
    1. 주어진 줄의 순서를 queue에 저장한다.
    2. 아래 한명씩 서는 공간을 stack으로 구현한다.
    3. 현재 간식을 받을 순서 i를 1부터 간식을 받을 때 마다 1씩 늘린다.
    4. queue에서 popleft할 때 i가 아니면 stack에 넣는다.
    5. queue가 다 비면 stack에서 pop하면서 순서에 맞게 간식을 먹을 수 있는지 확인한다.
'''
# 강의실 배정
'''
# 자료구조/알고리즘
    : heap
# 풀이방법
    1. 수업을 시작시간이 빠른 순으로 정렬한다.
    2. 끝나는 시간이 빠른 순으로 정렬되는 heap에 수업을 하나씩 넣는다.
    3. heap에서 pop된 수업이 끝나는 시간이 다음 수업이 시작되는 시간보다 빠르면 다음 수업을 push한다.
    4. heap에서 pop된 수업이 끝나는 시간이 다음 수업이 시작되는 시간보다 늦으면 pop한 것을 다시 push 하고 다음 수업을 push 한다
        : 강의실을 하나 더 개설한 효과
    5. 수업을 탐색했을 때 heap의 길이를 출력한다.
'''
# 연구소 3
'''
# 자료구조/알고리즘
    : bfs, 백트래킹
# 풀이방법
    1. 바이러스의 위치를 배열에 저장하고 combination을 이용해서 M개를 고르는 경우의 수를 뽑는다.
    2. 각 경우에 수에 대해서 완전탐색을 하는데 bfs를 통해서 바이러스가 연구소에 퍼지는 경우를 구한다.
    3. 2를 하는 도중에 현재 최솟값보다 많은 시간이 필요하면 백트래킹한다.
'''
# 직사각형 네개의 합집합의 면적 구하기
'''
# 자료구조/알고리즘
    : 이차원 배열, 완전탐색
# 풀이방법
    1. 100 * 100 크기의 이차원 배열을 만들고
    2. 각 직사각형이 차지하는 곳을 표시한다.
    3. 표시한 곳의 갯수를 센다.
'''
# 박스 채우기
'''
# 자료구조/알고리즘
    : dp, 그리디
# 풀이방법
    1. 가장 큰 큐브부터 채워나간다.
    2. 큐브 하나를 채우면 남은 구역은 3개의 직육면체로 쪼갤 수 있다.
    3. 각 정육면체에 대해서 1번을 재귀함수로 만들어서 돌린다.
'''
# 나무 재테크
'''
# 자료구조/알고리즘
    : 구현
# 풀이방법
    1. 이차원 배열을 만든다.
        : 각 좌표는 (양분, [심어진 나무들])로 표현된다.
    2. 각 계절에 해야할 연산을 함수로 만든다.
    3. K년 동안 시행하고 땅을 완전탐색하면서 심어진 나무들의 갯수를 센다.
'''
# 멀티탭 스케줄링
'''
# 자료구조/알고리즘
    : 그리디
# 풀이방법
    1. 멀티탭을 나타내는 빈 배열을 선언한다.
    2. 전기용품을 순서대로 탐색한다.
        1. 멀티탭에 자리가 있으면 꽂는다.
        2. 멀티탭에 이미 꽂혀있으면 pass
        3. 멀티탭이 꽉 차있다면 앞으로 쓰지 않을 기구를 뽑거나 가장 나중에 쓰는 기구를 뽑는다.
    3. 2에서 구한 뽑는 횟수를 출력한다.
'''
# 문제 이름
'''
# 자료구조/알고리즘
# 풀이방법
'''