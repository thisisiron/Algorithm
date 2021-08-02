import sys
import re
input = sys.stdin.readline


def is_slump(x):
    slump = re.compile('^([DE]F+)+G$')
    return slump.match(x)


def is_slimp(x):
    if len(x) < 2:
        return False

    if len(x) == 2 and x == 'AH':
        return True

    if x[0] == 'A' and x[-1] == 'C':
        if x[1] == 'B':
            return is_slimp(x[2:-1])
        else:
            return is_slump(x[1:-1])

    return False


N = int(input())
ans = []
print('SLURPYS OUTPUT')
for i in range(N):
    s = input().rstrip()

    try:
        c_idx = s.rindex('C')
    except ValueError:
        c_idx = -1
    if c_idx != -1:
        if is_slimp(s[0:c_idx + 1]) and is_slump(s[c_idx + 1:]):
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        ans.append('YES') if s.startswith('AH') and is_slump(s[2:]) else ans.append('NO')

print(*ans, sep='\n')
print('END OF OUTPUT')