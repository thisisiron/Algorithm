import sys 
input = sys.stdin.readline


N = int(input())

check = [False, False] + [True] * (N-1)
for i in range(2, int(N**0.5 + 1.5)):
    if check[i]:
        check[2 * i::i] = [False] * ((N - i) // i)
primes = [x for x in range(N+1) if check[x]]

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