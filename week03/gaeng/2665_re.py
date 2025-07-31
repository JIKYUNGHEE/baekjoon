from collections import deque
n = int(input())
maze = [list(map(int, input())) for _ in range(n)]

queue = deque()
queue.append((0,0))
visited = [[-1] * n for _ in range(n)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            cost = visited[x][y] + (1 if maze[nx][ny] == 0 else 0)
            if visited[nx][ny] == -1 or cost < visited[nx][ny]:
                visited[nx][ny] = cost     
                if maze[nx][ny] == 1:
                    queue.appendleft((nx, ny))
                else:
                    queue.append((nx, ny))

print(visited[n-1][n-1])
