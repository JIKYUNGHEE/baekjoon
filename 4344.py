case = int(input())

result = list()
for i in range(0, case):
    list = input().split()

    n = int (list[0])

    total = 0
    avg = 0
    for j in range(1, n + 1):
        total += int (list[j])
    
    avg = total / n
    cnt = 0
    for j in range(1, n + 1):
        if avg <  int (list[j]):
            cnt += 1

    result.append("%.3f%%" %((cnt / n) * 100))

for i in range(0, len(result)):
    print(result[i])

           
