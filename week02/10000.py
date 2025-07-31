n = int(input())
circles = []

for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x - r, x + r))  # 왼쪽 끝, 오른쪽 끝 저장

# 왼쪽 끝 기준으로 정렬 (같으면 오른쪽 끝 기준)
circles.sort()

stack = []
regions = 1  # 바깥 영역 1개로 시작

for left, right in circles:
    # 현재 원이 스택에 있는 것들과 겹치는지 확인
    while stack and stack[-1][1] <= left:
        stack.pop()
        regions += 1
    stack.append((left, right))



# 남은 스택에 있는 원들 처리
regions += len(stack)

print(regions)