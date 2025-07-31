from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for alist in adj:
    alist.sort()

visited = [False] * (N+1)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in adj[v]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
