from collections import deque

M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(layer)

visited = [[[False]* M for _ in range(N)] for _ in range(H)]
distance = [[[0] * M for _ in range(N)] for _ in range(H)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 1:
                queue.append((z, y, x))
                visited[z][y][x] = True
                distance[z][y][x] = 0

while queue:
    z, y, x = queue.popleft()
    for k in range(6):
        nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if not visited[nz][ny][nx] and tomatoes[nz][ny][nx] == 0:
                visited[nz][ny][nx] = True
                tomatoes[nz][ny][nx] = 1
                distance[nz][ny][nx] = distance[z][y][x] + 1
                queue.append((nz, ny, nx))

max_day = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 0:
                print(-1)
                exit()
            max_day = max(max_day, distance[z][y][x])
print(max_day)
