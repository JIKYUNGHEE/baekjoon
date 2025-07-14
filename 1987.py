n = int(input())

result = 0

numbers = list(map(int, input().split()))

for i in range(0, n):
    isSosu = True
    #소수 판별
    number = numbers[i]
    if number == 1:
        isSosu = False

    else:
        for j in range(1, number):
            if j == 1:
                continue
            if number % j == 0:
                isSosu = False

    if isSosu:
        result += 1

print(result)