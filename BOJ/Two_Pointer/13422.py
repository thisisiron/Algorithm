import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
	N, M, K = map(int, input().split())
	vill = [int(x) for x in input().split()]

	left = 0
	right = M

	total = sum(vill[:M])

	if N == M:
		print(1 if total < K else 0)
	else:
		cnt = 0 
		while left < N:
			if total < K:
				cnt += 1
			
			total -= vill[left]
			total += vill[right % N]

			left += 1
			right += 1
		print(cnt)