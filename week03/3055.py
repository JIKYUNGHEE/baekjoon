from collections import deque

R, C = map(int, input().split())

forest = [list(input().strip()) for _ in range(R)]

visited = [[False]* C for _ in range(R)]
distance = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queueW = deque()
queueS = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            queueS.append((i, j))
            visited[i][j] = True
            forest[i][j] = '.'
            distance[i][j] = 0
        if forest[i][j] == '*':
            queueW.append((i, j))

def spread():
    for _ in range(len(queueW)):
        x, y = queueW.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if forest[nx][ny] == '.':
                    forest[nx][ny] = '*'
                    queueW.append((nx, ny))

def move():
    for _ in range(len(queueS)):
        x, y = queueS.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny]:
                    if forest[nx][ny] == 'D':
                        print(distance[x][y] + 1)
                        exit()
                    if forest[nx][ny] == '.':
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                        queueS.append((nx, ny))

while queueS:
    spread()
    move()

print("KAKTUS")