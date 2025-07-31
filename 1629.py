a, b, c = map(int, input().split())

def multiply(a, b, c):
    if b == 1:
        return a % c

    half = multiply(a, b//2, c)
    result = (half * half) % c

    if b % 2 == 1:
        result = (result * a) % c
    
    return result

print(multiply(a, b, c))