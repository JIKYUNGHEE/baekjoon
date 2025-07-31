def can_install(houses, C, dist):
    count = 1
    last = houses[0]
    for x in houses[1:]:
        if x - last >= dist:
            count += 1
            last = x
            if count >= C:
                return True
    return False

n, c = map(int, input().split())
houses = list()
for _ in range(n):
    houses.append(int(input()))
houses.sort()

low, high = 1, houses[-1] - houses[0]
answer = 0
while low <= high:
    mid = (low + high) // 2
    if can_install(houses, c, mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)