n = int(input())

commands = list()

for i in range(n):
    command = input()
    commands.append(command)

stack = list()
for command in commands:
    if command.startswith("push"):
        stack.append(command.split()[1])
    
    if command.startswith("top"):
        if len(stack) > 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)
    
    if command.startswith("size"):
        print(len(stack))

    if command.startswith("empty"):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        
    if command.startswith("pop"):
        if len(stack) > 0:
            num = stack[len(stack) - 1]
            print(num)
            stack = stack[:(len(stack) - 1)]
        else:
            print(-1)
    