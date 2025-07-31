from collections import deque

M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
 layer = [list(map(int, input().split())) for _ in range(N)]
 tomatoes.append(layer)

visited = [[[False] * M for _ in range(N)] for _ in range(H)]
days = [[[0] * M for _ in range(N)] for _ in range(H)]

dz = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dx = [-1, 1, 0, 0, 0, 0]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 1:
                visited[z][y][x] = True
                days[z][y][x] = 0
                queue.append((z, y, x))

while queue:
    z, y, x = queue.popleft()

    for k in range(6):
        nz, ny, nx = z + dz[k], y + dy[k], x + dx[k]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if not visited[nz][ny][nx] and tomatoes[nz][ny][nx] == 0:
                    tomatoes[nz][ny][nx] = 1
                    visited[nz][ny][nx] = True
                    days[nz][ny][nx] = days[z][y][x] + 1
                    queue.append((nz, ny, nx))
max_day = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 0:
                print(-1)
                exit()
            max_day = max(max_day, days[z][y][x])

print(max_day)