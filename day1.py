import sys
sys.stdin=open("input.txt", "r")

n = int(input())
weights = list(map(int, input().split()))

weights.sort(reverse=True)

def canMeasure(x, weights):
    for weight in weights:
        if x == weight:
            return True
        elif x > weight:
            x -= weight
        else:
            continue
    return False

count = 1

while canMeasure(count, weights):
    count += 1

print(count)
