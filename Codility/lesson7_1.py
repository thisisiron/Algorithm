def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if s in ['(', '{', '[']:
            stack.append(s)
        elif s in [')', '}', ']']:
            if len(stack) == 0:  # time cutting
                return 0
            x = stack.pop()
            if x == '(' and s != ')':
                return 0
            elif x == '{' and s != '}':
                return 0
            elif x == '[' and s != ']':
                return 0
    if len(stack) != 0:
        return 0
    return 1
