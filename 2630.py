n = int(input())

inputs = list()

for i in range(n):
    inputs.append(list(map(int, input().split())))

cnt = [0, 0]

def sol(x, y, size):
    if size < 1:
        return
    
    total = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            total += inputs[i][j]

    if total == size * size:
        cnt[1] += 1
        return
    
    elif total == 0:
        cnt[0] += 1
        return
    
    else:
        half = size // 2
        sol(x, y, half)        
        sol(x + half, y, half)
        sol(x, y + half, half)
        sol(x + half, y + half, half)

sol(0, 0, n)
print(cnt[0])
print(cnt[1])