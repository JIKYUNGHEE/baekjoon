from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[False]* M for _ in range(N)]
distance = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append(0,0)
visited[0][0] = True
distance[0][0] = 1

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                queue.append(nx, ny)

print(distance[N-1][M-1])