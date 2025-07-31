import sys

n = int(sys.stdin.readline())

count = [0] * 10001
for i in range(0, n):
    k = int(sys.stdin.readline())
    count[k] += 1

for i in range(10001):
    v = count[i]
    if v > 0:
        for j in range(v):
            print(i)