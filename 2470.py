n = int(input())

array = list(map(int, input().split()))

array.sort()

left = 0
right = n - 1
best_sum = float('inf')
answer = list()

while left < right:
    current_sum = array[left] + array[right]

    if abs(current_sum) < best_sum:
        best_sum = abs(current_sum)
        answer = [array[left], array[right]]
    
    if current_sum < 0:
        left += 1
    else:
        right -= 1
    
print(answer[0], answer[1])