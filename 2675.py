t = int(input())

result = list()
for i in range(0, t):
    rs = input().split()
    r = int(rs[0])
    
    s = rs[1]
    newS = ""
    for j in range(0, len(s)):
        ch = s[j]
        for k in range(0, r):
            newS = newS + ch
    
    result.append(newS)

for i in range(0, len(result)):
    print(result[i])
