import sys
input = sys.stdin.readline


N, K = map(int, input().split())

bag = {0: 0} 

for _ in range(N):
    w, v = map(int, input().split())
    temp = {}        
    
    for dw, dv in bag.items():
        nw, nv = dw + w, dv + v
        if nw <= K and bag.get(nw, 0) < nv:
            temp[nw] = nv
    bag.update(temp)
print(max(bag.values()))