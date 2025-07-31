n = int(input())

tests = list()
for i in range(n):
    vps = input()
    tests.append(vps)

for test in tests:
    stack = list()
    word = "NO"
    flag = False
    for i in range(len(test)):
        if test[i] == "(":
            stack.append("(")
        else: # ")"
            if len(stack) == 0:
                word = "NO"
                flag = True
                break
            else:
                stack = stack[:len(stack) - 1]
    
    if len(stack) == 0 and (not flag):
        word = "YES"

    print(word)