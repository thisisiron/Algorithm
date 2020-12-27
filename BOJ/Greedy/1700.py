import sys
input = sys.stdin.readline


N, K = map(int, input().split())
items = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(len(items)):
    if items[i] in plug:
        continue

    if len(plug) < N:
        plug.append(items[i])
        continue

    candi = []
    
    for j in range(N):
        idx = 0
        for k in range(i + 1, K):
            if items[k] == plug[j]:
                break
            idx += 1
        candi.append(idx)
    plug_out = candi.index(max(candi))
    del plug[plug_out]
    plug.append(items[i])
    cnt += 1
print(cnt)
