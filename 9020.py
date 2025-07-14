
def isSosu(n: int) -> bool:
    for i in range(1, n-1):
        if i == 1:
            continue
        if n % i == 0:
            return False
    return True


t = int(input())

inputs = list()

for i in range(0, t):
    inputs.append(int(input()))

for i in range(0, len(inputs)):
    num = inputs[i]
    
    for j in range(num//2, 1, -1):
        if isSosu(j) and isSosu(num - j):
            print(f'{j} {num-j}')
            break

        

