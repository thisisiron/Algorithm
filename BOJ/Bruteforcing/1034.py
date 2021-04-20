import sys
input = sys.stdin.readline


N, M = map(int, input().split())

lamps = []
for _ in range(N):
    lamps.append(input().rstrip())
K = int(input())
mx = 0

for row in range(N):
    zero = 0
    for col in range(M):
        if lamps[row][col] == '0':
            zero += 1
    
    on_lamp = 0
    if zero <= K and zero % 2 == K % 2:
        for r in range(N):
            if lamps[row] == lamps[r]:
                on_lamp += 1

    if mx < on_lamp:
        mx = on_lamp
print(mx)