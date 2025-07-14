max = 0;
pos = 0;
for i in range(0, 9):
    a = int(input())
    if max < a:
        max = a
        pos = i + 1

print(max)
print(pos)