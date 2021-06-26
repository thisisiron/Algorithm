import sys
input = sys.stdin.readline


S = list(input().rstrip())
T = list(input().rstrip())

same = 0

while True:
	if len(S) == len(T):
		if S == T:
			same = 1 
		break

	c = T[-1]
	T.pop()
	if c == 'B':
		T = T[::-1]

print(same)