import sys
input = sys.stdin.readline


N = int(input())
dices = []

for _ in range(N):
    dices.append([int(x) for x in input().split()])

route = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
mx = 0

for i in range(6):
    res = []
    tmp = [1,2,3,4,5,6]
    tmp.remove(dices[0][i])
    nxt = dices[0][route[i]]
    tmp.remove(nxt)
    res.append(max(tmp))
    for j in range(1, N):
        tmp = [1,2,3,4,5,6]
        tmp.remove(nxt)
        nxt = dices[j][route[dices[j].index(nxt)]]
        tmp.remove(nxt)
        res.append(max(tmp))
    res = sum(res)
    if mx < res:
        mx = res
print(mx)