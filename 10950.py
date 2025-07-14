case = int(input())

list = list()
for i in range(1, case + 1):
    a, b = map(int, input().split())
    list.append(a + b)

for i in range(0, case):
    print(list[i])