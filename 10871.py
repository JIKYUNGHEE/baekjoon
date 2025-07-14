n, x = map(int, input().split())

list = input().split()

for i in range(0, n):
    if int(list[i]) < x:
        print(list[i]+ " ", end="")