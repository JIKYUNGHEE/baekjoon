import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = []

for i in a:
    idx = bisect_left(b, i)
    if idx == len(b):
        b.append(i)
    else:
        b[idx] = i

print(len(b))