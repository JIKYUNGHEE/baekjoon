def nsum(n):
    total = 0
    for i in range (n+1):
        total += i
    return total


def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

def expt(b, n):
    if n == 0:
        return 1
    return b * expt(b, n-1)

def fastExpt(b, n):
    if n == 0:
        return 1

        if n % 2 == 0:
            return fastExpt(b, n//2) * fastExpt(b, n//2)
        else:
            return b * fastExpt(b, n - 1)

def count_ways(amount, coins, index=0):
    if amount == 0:
        return 1
    if amount < 0 or index == len(coins):
        return 0
    
    use_it = count_ways(amount - coins[index], coins, index)
    skip_it = count_ways(amount, coins, index + 1)

    return use_it + skip_it

print(count_ways(10, [2, 5, 3, 6]))

def char_way(chars, n):
    if n == 0:
        return 1
    else:
        return char_way(chars, n - 1) * len(chars)

print(char_way("abc", 4))