import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

dp = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))   # (상위 부품, 필요 개수)
    indegree[X] += 1

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:   # 기본 부품
        queue.append(i)
        dp[i][i] = 1

while queue:
    cur = queue.popleft()
    for nxt, cnt in graph[cur]:
        for i in range(1, N+1):
            dp[nxt][i] += dp[cur][i] * cnt
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

for i in range(1, N+1):
    if dp[N][i] > 0:
        print(i, dp[N][i])
