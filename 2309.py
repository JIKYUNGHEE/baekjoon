nan = []

for _ in range(9):
    nan.append(int(input()))

total = sum(nan)

for i in range(9):
    for j in range(i + 1, 9):
        if total - nan[i] - nan[j] == 100:
            fake1, fake2 = nan[i], nan[j]
            nan_copy = nan[:]
            nan_copy.remove(fake1)
            nan_copy.remove(fake2)
            nan_copy.sort()
            for h in nan_copy:
                print(h)
            exit()