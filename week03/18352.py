import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

visited = [-1] * (N + 1)
visited[X] = 0
queue = deque([X])

while queue:
    v = queue.popleft()
    for nxt in adj[v]:
        if visited[nxt] == -1:
            visited[nxt] = visited[v] + 1
            queue.append(nxt)

result = [i for i in range(1, N+1) if visited[i] == K]
if not result:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')