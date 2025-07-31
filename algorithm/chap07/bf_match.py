# 브루트 포스법으로 문자열 검색하기

def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0  #txt를 따라가는 커서
    pp = 0  #pat를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp +=1
        else:
            pt = pt - pp + 1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1
