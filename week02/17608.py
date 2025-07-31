import sys

n = int(sys.stdin.readline())
stack = list()
for i in range(n):
    stack.append(int(sys.stdin.readline()))

count = 0
max_height = 0

while len(stack) != 0:
    now = stack.pop()
    if now > max_height:
        count += 1
        max_height = now

print(count)