n = int(input())

if n < 100:
    count = n
    print(count)

else:
    count = 99
    for i in range(100, n + 1):
        char_list = list(str(i))
        diff = int(char_list[1]) - int(char_list[0])
        if (int(char_list[2]) - int(char_list[1])) == diff:
            count += 1
    
    print(count)