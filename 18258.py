import sys
from collections import deque

n = int(sys.stdin.readline())

commands = list()
queue = deque()

for i in range(n):
    command = sys.stdin.readline()
    commands.append(command)

for command in commands:
    if command.startswith("push"):
        queue.append(command.split()[1])

    if command.startswith("front"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        
    if command.startswith("back"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        
    if command.startswith("size"):
        print(len(queue))

    if command.startswith("empty"):
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    if command.startswith("pop"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            