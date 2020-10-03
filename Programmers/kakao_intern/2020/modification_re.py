from itertools import permutations


def solution(expression: str):
    priorities: list = list(permutations(['*', '+', '-']))

    mx: int = 0
    for prior in priorities:
        mx = max(mx, abs(int(calc(expression, prior, 0))))

    return mx 


def calc(expression, prior, n):
    if n == 2:
        return str(eval(expression))
    if prior[n] == '*':
        res = eval('*'.join([calc(e, prior, n+1) for e in expression.split('*')]))
    if prior[n] == '+':
        res = eval('+'.join([calc(e, prior, n+1) for e in expression.split('+')]))
    if prior[n] == '-':
        res = eval('-'.join([calc(e, prior, n+1) for e in expression.split('-')]))
    return str(res)


if __name__ == '__main__':
    print(solution("100-200*300-500+20"), '\n')
    print(solution("100-200*300+500-20"), '\n')
    print(solution("50*6-3*2"), '\n')
    print(solution("50*6+3*2"), '\n')