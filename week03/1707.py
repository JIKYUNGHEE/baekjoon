from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node, color):
    visited[node] = color
    for nxt in graph[node]:
        if visited[nxt] == 0:
            if not dfs(nxt, -color):
                return False
        elif visited[nxt] == visited[node]:
                return False
    return True

def bfs(node, color):
    queue = deque([node])
    visited[node] = color

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = -visited[cur]
                queue.append(nxt)
            elif visited[nxt] == visited[cur]:
                return False
    return True
    

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * (V + 1)

    is_bipartite = True

    for i in range(1, V + 1):
        if visited[i] == 0:
            #if not dfs(i, 1):
            if not bfs(i, 1):
                is_bipartite = False
                break
    
    print("YES" if is_bipartite else "NO")