from itertools import permutations
from collections import deque


def solution(expression: str):
    answer: int = 0
    priors: list = list(permutations(['*', '+', '-']))


    mx: int = 0
    for prior in priors:
        print(prior)
        mx = max(mx, cal(expression, prior))
        print(mx, '\n')

    return mx 


def cal(expression: str, prior: tuple):
    for op in prior[:-1]:
        i: int = 0
        stack: deque = deque() 
        while i < len(expression):
            if op == expression[i]:
                pre: str = ""

                while stack and stack[-1] not in prior: 
                    pre += stack.pop() 
                if len(stack) == 1 and stack[0] in prior:
                    pre += stack.pop() 
                pre = pre[::-1]

                j: int = i + 1
                if expression[j] in prior:
                    j += 1
                while j < len(expression) and expression[j] not in prior:
                    j += 1
                pre += expression[i:j] 

                for a in str(eval(pre)):
                    stack.append(a)
                i = j 

            else:
                stack.append(expression[i])
                i += 1
            
        expression = ''.join(stack)
    # print(expression)
    return abs(eval(expression))


if __name__ == '__main__':
    print(solution("100-200*300-500+20"), '\n')
    print(solution("100-200*300+500-20"), '\n')
    print(solution("50*6-3*2"), '\n')
    print(solution("50*6+3*2"), '\n')