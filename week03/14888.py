N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')

def dfs(idx, sum):
    global max_value, min_value
    
    if idx == N:
        max_value = max(sum, max_value)
        min_value = min(sum, min_value)
        return

    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            if i == 0:
                dfs(idx + 1, sum + nums[idx])
            elif i == 1:
                dfs(idx + 1, sum - nums[idx])
            elif i == 2:
                dfs(idx + 1, sum * nums[idx])
            else:
                if sum < 0:
                    dfs(idx + 1, -(-sum // nums[idx]))
                else:
                    dfs(idx + 1, sum // nums[idx])
            oper[i] += 1

dfs(1, nums[0])
print(max_value)
print(min_value)