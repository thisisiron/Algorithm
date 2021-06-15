import sys
input = sys.stdin.readline


def update(cur, val):
	while cur > 0:
		tree[cur] += val
		cur //= 2


def sum_interval(start, end):
	total = 0
	while start <= end:
		if start % 2 == 1:
			total += tree[start]
		if end % 2 == 0:
			total += tree[end]
		start = (start + 1) // 2
		end = (end - 1) // 2
	return total


N, M , K = map(int, input().split())
tree = [0] * 4 * N
start_idx = 1
while start_idx < N:
	start_idx *= 2
start_idx -= 1

for i in range(1, N + 1):
	tree[i + start_idx] = int(input())

for i in range(start_idx, -1, -1):
	tree[i] = tree[i * 2] + tree[i * 2 + 1]

for _ in range(M + K):
	a, b, c = map(int, input().split())
	if a == 1:
		update(start_idx + b, c - tree[start_idx + b])	
	elif a == 2:
		print(sum_interval(start_idx + b, start_idx + c))