import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
info = list(input().strip())  # '0' = 실외, '1' = 실내

graph = [[] for _ in range(N+1)]
ans = 0

# 간선 입력
for _ in range(N-1):
    u, v = map(int, input().split())

    # 실내-실내 바로 연결된 경우: 경로 2개 (양방향)
    if info[u-1] == '1' and info[v-1] == '1':
        ans += 2
    else:
        graph[u].append(v)
        graph[v].append(u)

visited = [False] * (N+1)

def dfs(node):
    """실외 컴포넌트 탐색, 인접 실내 노드 개수 반환"""
    visited[node] = True
    cnt = 0
    for nxt in graph[node]:
        if info[nxt-1] == '1':  # 실내
            cnt += 1
        elif not visited[nxt]:  # 실외
            cnt += dfs(nxt)
    return cnt

# 모든 실외 노드 탐색
for i in range(1, N+1):
    if info[i-1] == '0' and not visited[i]:
        k = dfs(i)   # 해당 실외 컴포넌트와 연결된 실내 개수
        ans += k * (k - 1)

print(ans)
