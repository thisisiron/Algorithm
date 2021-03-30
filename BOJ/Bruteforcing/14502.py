import sys
import copy
input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def make_wall(start, cnt):
    global mx
    if cnt == 3:
        new_lab = copy.deepcopy(lab)
        for i in range(len(virus)):
            v_y, v_x = virus[i]
            spread_virus(v_y, v_x, new_lab)
        safe_cnt = sum(row.count(0) for row in new_lab) 
        if mx < safe_cnt:
            mx = safe_cnt 
    else:
        for i in range(start, N * M):
            nxt_y = i // M
            nxt_x = i % M
            if lab[nxt_y][nxt_x] == 0:
                lab[nxt_y][nxt_x] = 1
                make_wall(i, cnt + 1)
                lab[nxt_y][nxt_x] = 0
    

def spread_virus(y, x, new_lab):
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
            continue
        if new_lab[new_y][new_x] == 0:
            new_lab[new_y][new_x] = 2
            spread_virus(new_y, new_x, new_lab)


N, M = map(int, input().split())
virus = []
lab = []
for r in range(N):
    arr = list(map(int, input().split()))
    for c, x in enumerate(arr):
        if x == 2:
            virus.append((r, c))
    lab.append(arr)

mx = 0 
make_wall(0, 0)

print(mx)