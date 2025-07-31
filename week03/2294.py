from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

visited = [False] * (k + 1)
queue = deque()
queue.append((0,0))
visited[0] = True

while queue:
    current, count = queue.popleft()

    for coin in coins:
        next_money = current + coin
        if next_money > k:
            continue
        if next_money == k:
            print(count + 1)
            exit()
        if not visited[next_money]:
            visited[next_money] = True
            queue.append(next_money, count + 1)

print(-1)