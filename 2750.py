n = int(input())

list = list()
for i in range(0, n):
    list.append(int(input()))

"""버블정렬"""
for i in range(n-1):
    for j in range(n-1, i, -1):
        if list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]

for i in range(0, n):
    print(list[i])