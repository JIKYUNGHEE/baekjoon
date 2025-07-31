from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n + 1))
array = list()

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    array.append(queue.popleft())

print('<' + ', '.join(map(str, array)) + '>')