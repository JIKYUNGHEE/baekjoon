def can_install(houses, c, dist):
    count = 1
    last = houses[0]
    for x in houses[1:]:
        if x - last >= dist:
            count += 1
            last = x
            if count >= c:
                return True
    return False

n, c = map(int, input().split())
houses = list()
for _ in range(n):
    houses.append(int(input()))
houses.sort()

min = 1
max = houses[-1] - houses[0]
answer = 0
while min <= max:
    mid = (min + max) // 2
    if can_install(houses, c, mid):
        answer = mid
        min = mid + 1
    else:
        max = mid - 1
print(answer)
