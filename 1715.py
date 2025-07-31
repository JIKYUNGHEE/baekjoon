import sys
import heapq

n = int(input())

heap = []
total = 0

for _ in range(n):
    x = int(input())
    heapq.heappush(heap, x)

while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    cost = x + y
    total += cost
    heapq.heappush(heap, cost)

print(total)