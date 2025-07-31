from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*result)