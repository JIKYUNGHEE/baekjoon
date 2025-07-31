from collections import deque

n = int(input())
v = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(v):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
def dfs(v):
    visited[v] = True
    for nxt in adj[v]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

#dfs(1)
bfs(1)
count = 0
for vi in visited:
    if vi:
        count += 1

print(count - 1)