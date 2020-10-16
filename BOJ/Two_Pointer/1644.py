import sys 
input = sys.stdin.readline

N = int(input())

primes = []
check = [False] * (N + 1) 
for i in range(2, N + 1):
    if check[i] == False:
        for j in range(i * 2, N + 1, i):
            check[j] = True

for i in range(2, N + 1):
    if not check[i]:
        primes.append(i)

start = 0
end = 0
result = 0
cnt = 0

while True:
    if result >= N:
        if result == N:
            cnt += 1
        result -= primes[start]
        start += 1
    elif end == len(primes):
        break 
    else:
        result += primes[end]
        end += 1
print(cnt)