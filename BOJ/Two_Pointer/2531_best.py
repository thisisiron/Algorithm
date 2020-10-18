import sys
input = sys.stdin.readline


N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]

check = [0] * (d + 1)
check[c] = 1
cnt = 1  # 초밥 종류
answer = 0  # 최대값

for i in range(k):
    if check[sushis[i]] == 0:
        print(sushis[i])
        cnt += 1
    check[sushis[i]] += 1
    sushis.append(sushis[i])

for i in range(N):
    answer = max(answer, cnt)

    # 가장 처음에 있는 초밥을 제거 
    check[sushis[i]] -= 1 
    if check[sushis[i]] == 0:
        cnt -= 1
    
    # 가장 마지막에 있는 초밥 추가 
    if check[sushis[i + k]] == 0:
        cnt += 1

    check[sushis[i + k]] += 1

print(answer)