w, h = map(int, input().split())
n = int(input())

listW = list()
listH = list()

listW.append(0)
listW.append(w)

listH.append(0)
listH.append(h)

for i in range(0, n):
    x, y = map(int, input().split())
    if x == 0:
        listH.append(y)
    else:
        listW.append(y)

listW.sort()
listH.sort()

maxW = 0
maxH = 0

for i in range(1, len(listW)):
    if  maxW < (listW[i] - listW[i-1]):
        maxW = listW[i] - listW[i-1]

for i in range(1, len(listH)):
    if  maxH < (listH[i] - listH[i-1]):
        maxH = listH[i] - listH[i-1]

print(maxW * maxH)