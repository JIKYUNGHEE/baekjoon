t = int(input())

tests = []
d = [0] * 12
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(t):
    n = int(input())
    tests.append(n)

def count_ways(test):
    if test < 4:
        return d[test]
    
    if test > 11:
        return 0
    
    for i in range(4, test + 1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    return d[test]


for test in tests:
    print(count_ways(test))