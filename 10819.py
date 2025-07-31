n = int(input())

a = list(map(int, input().split()))

max_result = 0

def permute(arr, path):
    global max_result

    if not arr:
        total = 0
        for i in range(len(path) - 1):
            total += abs(path[i] - path[i + 1])

        max_result = max(max_result, total)
        return

    for i in range(len(arr)):
        permute(arr[:i] + arr[i+1:], path + [arr[i]])
    
permute(a, [])
print(max_result)