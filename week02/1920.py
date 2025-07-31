n = int(input())
arrayN = list(map(int, input().split()))

m = int(input())
arrayM = list(map(int, input().split()))

arrayN.sort()

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

for target in arrayM:
    if binary_search(arrayN, target):
        print(1)
    else:
        print(0)