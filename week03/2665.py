from collections import deque

N = int(input())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1]*N for _ in range(N)]
queue = deque()
queue.append((0, 0))
visited[0][0] = 0

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            cost = visited[x][y] + (1 if maze[nx][ny] == 0 else 0)
            if visited[nx][ny] == -1 or visited[nx][ny] > cost:
                visited[nx][ny] = cost
                if maze[nx][ny] == 1:
                    queue.appendleft((nx, ny))
                else:
                    queue.append((nx, ny))

print(visited[N-1][N-1])
