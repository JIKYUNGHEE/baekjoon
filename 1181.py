n = int(input())

wordList = []
for i in range(n):
    s = input()
    if s not in wordList:
        wordList.append(s)

# 정렬: 먼저 길이순, 그다음 사전순
wordList.sort(key=lambda x: (len(x), x))

# 출력
for word in wordList:
    print(word)