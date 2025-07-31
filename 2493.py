n = int(input())
heights = list(map(int, input().split()))

stack = []
result = []

for i in range(n):
    current_height = heights[i]

    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])
    
    stack.append((i+1, current_height))

print(' '.join(map(str, result)))