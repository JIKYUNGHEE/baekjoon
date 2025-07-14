x, y, w, h = map(int, input().split())

min = 1000

wx = w - x
hy = h - y

if min > x:
    min = x

if min > y:
    min = y

if min > wx:
    min = wx

if min > hy:
    min = hy

print(min)