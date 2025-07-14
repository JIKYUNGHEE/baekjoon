

pos = [0] * 8
flag = [False] * 8

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i:int) -> None:
    """i열에 퀸을 배치"""
    for j in range(8):
        if not flag[j]: #j행에 퀸을 배치하지 않았으면
            pos[i] = j
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False

set(0)