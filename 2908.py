a, b = map(int, input().split())

strA = str(a)
newA = int(strA[2] + strA[1] + strA[0])

strB = str(b)
newB = int(strB[2] + strB[1] + strB[0])

if newA > newB:
    print(newA)
else:
    print(newB)

