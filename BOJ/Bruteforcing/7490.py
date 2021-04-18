import sys
input = sys.stdin.readline


def backtraking(form):
    if len(form) == (2 * N - 1):
        tmp = form.replace(' ', '')
        res = eval(tmp)
        if res == 0:
            ans.append(form)
    else:
        if len(form) % 2 == 0:
            backtraking(form + str(int(form[-2]) + 1))
        else:
            backtraking(form + ' ')
            backtraking(form + '+')
            backtraking(form + '-')


T = int(input())
for _ in range(T):
    ans = []
    N = int(input())
    backtraking('1')
    print(*ans, sep='\n')
    print()