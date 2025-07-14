year = (int)(input())

isYoon = False

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        isYoon = True

if isYoon:
    print(1)
else:
    print(0)