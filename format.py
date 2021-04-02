import sys
sys.stdin=open("input.txt", "r")

li = []

for i in range(19):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
