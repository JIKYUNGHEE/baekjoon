import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
def dfs(current, graph, parent):
    for neighbor in graph[current]:
        if parent[neighbor] == 0:
            parent[neighbor] = current
            dfs(neighbor, graph, parent)

parent[1] = 1
dfs(1, graph, parent)

for i in range(2, N+1):
    print(parent[i])