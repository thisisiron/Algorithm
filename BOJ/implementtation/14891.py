import sys
from collections import deque
input = sys.stdin.readline


def check_right(cur, dirc):
    if cur > 4 or wheel[cur - 1][right] == wheel[cur][left]:
        return
    if wheel[cur - 1][right] != wheel[cur][left]:
        check_right(cur + 1, -dirc)
        wheel[cur].rotate(dirc)


def check_left(cur, dirc):
    if cur < 1 or wheel[cur][right] == wheel[cur + 1][left]:
        return
    if wheel[cur][right] != wheel[cur + 1][left]:
        check_left(cur - 1, -dirc)
        wheel[cur].rotate(dirc)

# N -> 0, S -> 1
wheel = {
    1: deque([int(x) for x in input().rstrip()]),
    2: deque([int(x) for x in input().rstrip()]),
    3: deque([int(x) for x in input().rstrip()]),
    4: deque([int(x) for x in input().rstrip()])
}

left = 6
right = 2

k = int(input())
for i in range(k):
    idx, dirc = map(int, input().split())
    check_right(idx + 1, -dirc)
    check_left(idx - 1, -dirc)
    wheel[idx].rotate(dirc)

ans = 0
for i in range(1, 5):
    ans += (2**(i - 1)) * wheel[i][0]
print(ans)