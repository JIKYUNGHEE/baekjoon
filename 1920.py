n = int(input())
arrayN = list(map(int, input().split()))
arrayN.sort()

m = int(input())
arrayM = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


for target in arrayM:
    if binary_search(arrayN, target):
        print(1)
    else:
        print(0)