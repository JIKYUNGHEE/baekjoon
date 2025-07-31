import sys

def largest_rectangle(hist):
    stack = []
    max_area = 0
    index = 0
    hist.append(0)  # 끝까지 처리하기 위해 0 추가

    while index < len(hist):
        # 스택이 비었거나 현재 높이가 더 높으면 push
        if not stack or hist[stack[-1]] <= hist[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = hist[top] * width
            max_area = max(max_area, area)

    return max_area

while True:
    line = sys.stdin.readline()
    if not line:
        break
    nums = list(map(int, line.strip().split()))
    if nums[0] == 0:
        break
    n = nums[0]
    histogram = nums[1:]
    print(largest_rectangle(histogram))
