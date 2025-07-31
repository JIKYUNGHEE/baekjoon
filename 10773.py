k = int(input())

stack = list()

for i in range(k):
    n = int(input())
    if n == 0:
        stack = stack[:len(stack) - 1]
    else:
        stack.append(n)

print(sum(stack))