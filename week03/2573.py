import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
sea_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0

def dfs(x, y, visited):
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if sea_map[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny, visited)

def count_components(icebergs):
    visited = [[False] * M for _ in range(N)]  # 매번 초기화
    cnt = 0
    for x, y in icebergs:
        if sea_map[x][y] > 0 and not visited[x][y]:
            dfs(x, y, visited)
            cnt += 1
    return cnt

def melt(icebergs):
    new_iceberg = []
    temp = [[0] * M for _ in range(N)]  # 동시에 녹이기 위해 감소량 저장
    for x, y in icebergs:
        cnt = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and sea_map[nx][ny] == 0:
                cnt += 1
        temp[x][y] = cnt


    for x, y in icebergs:
        new_h = max(0, sea_map[x][y] - temp[x][y])
        sea_map[x][y] = new_h
        if new_h > 0:
            new_iceberg.append((x, y))
            
    return new_iceberg

# 처음 얼음 좌표 모으기
icebergs = [(i, j) for i in range(N) for j in range(M) if sea_map[i][j] > 0]

while True:
    count = count_components(icebergs)
    if count == 0:
        print(0)
        break
    elif count >= 2:
        print(year)
        break
    
    icebergs = melt(icebergs)
    year += 1