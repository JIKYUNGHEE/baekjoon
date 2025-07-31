n = int(input())

count = 0
original = n

while True:
    a = n // 10
    b = n % 10
    c = b * 10 + (a + b)%10

    count += 1

    n = c

    if n == original:
        break

print(count)