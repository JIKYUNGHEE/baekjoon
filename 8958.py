case = int(input())

list = list()

for i in range(0, case):
    result = [c for c in input()]

    totalScore = 0
    score = 0
    for j in range(0, len(result)):
        ox = result[j]
        if ox == "O":
            score += 1
            totalScore += score
        else:
            score = 0
    list.append(totalScore)


for i in range(0, len(list)):
    print(list[i])
