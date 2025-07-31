import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for W, V in items:
    # 뒤에서 앞으로 업데이트해야 같은 물건을 여러 번 안 쓰게 됨
    for w in range(K, W - 1, -1):
        dp[w] = max(dp[w], dp[w - W] + V)

print(dp[K])