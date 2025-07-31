from collections import deque

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

queue = deque()
queue.append((0, 0))
visited = [[False] * M for _ in range (N)]
distance = [[0] * M for _ in range(N)]
distance[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

print(distance[N-1][M-1])