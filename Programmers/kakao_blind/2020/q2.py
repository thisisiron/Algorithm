def solution(p):
    if check(p):
        return p
    return split(p)


def replace(u: str, v: str) -> str:
    result = '('
    result += v + ')'
    for c in u:
        if c == '(':
            result += ')'
        else:
            result += '('
    return result
        

def check(s: str) -> bool:
    is_ok: bool = False 
    stack: list = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False 
            stack.pop()
    return True


def split(s: str) -> list:
    if len(s) == 0:
        return s
    left: int = 0
    right: int = 0
        
    for idx, c in enumerate(s):
        if c == '(':
            left += 1
        else:
            right += 1
        if left == right:
            if s[idx] == ')':
                return s[:idx + 1] + split(s[idx + 1:])
            else:
                return replcae(s[1:idx], split(s[idx + 1:]))
    return s, '' 