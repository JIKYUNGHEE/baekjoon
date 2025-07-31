n, k = map(int, input().split())
number = input().strip()

result = []

for digit in number:
    while result and k > 0 and result[-1] < digit:
        result.pop()
        k -= 1
    result.append(digit)
    
while k > 0:
    result.pop()
    k -= 1

print(''.join(result))