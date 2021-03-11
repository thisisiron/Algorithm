import sys
input = sys.stdin.readline


def backtracking(cnt):
    for i in range(1, (cnt // 2) + 1):
        if ans[-i:] == ans[-2 * i:-i]:
            return False 

    if cnt == N:
        print(*ans, sep='')
        return True 
    else:
        for i in range(3):
            ans.append(number[i])
            if backtracking(cnt + 1): 
                return True 
            ans.pop()


N = int(input())
number = [1, 2, 3]
ans = []
backtracking(0)