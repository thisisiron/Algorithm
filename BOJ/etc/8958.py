import sys
input = sys.stdin.readline


T = int(input())
for t in range(T):
    ox = input().rstrip()
    score = 0
    check = 1
    for i in range(len(ox)):
        if ox[i] == 'X':
            check = 1
        else:
            score += check
            check += 1
    print(score)