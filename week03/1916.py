import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 이미 더 짧은 경로를 찾았으면 무시
        if current_dist > dist[u]:
            continue

        # 목적지에 도착하면 바로 종료 가능
        if u == end:
            return dist[u]

        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist[end]


n = int(input())   # 도시 개수
m = int(input())   # 버스 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))  # 방향 그래프

start, end = map(int, input().split())

print(dijkstra(start, end, graph, n))