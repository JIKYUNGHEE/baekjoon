T = int(input())
result = []
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    dp = [0] * (total + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, total+1):
            dp[x] += dp[x - coin]
        
    result.append(dp[total])

print(*result, sep='\n')