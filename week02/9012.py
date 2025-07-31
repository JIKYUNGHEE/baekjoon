import sys
input = sys.stdin.readline

def is_vps(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if not stack:
                return False
            stack.pop()
    return not stack


T = int(input())
for _ in range(T):
    line = input().strip()
    print("YES" if is_vps(line) else "NO")