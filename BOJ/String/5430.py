import sys
input = sys.stdin.readline


def AC(cmds, arr):
	cmds.replace('RR', '')
	l, r, d = 0, 0, True
	for c in cmds:
		if c == 'R':
			d = not d
		elif c == 'D':
			if d:
				l += 1
			else:
				r += 1

	if l + r <= n:
		res = [str(x) for x in arr[l:n - r]]
		if d:
			print('[' + ','.join(res) + ']')
		else:
			print('[' + ','.join(res[::-1]) + ']')
	else:
		print('error')

T = int(input())

for _ in range(T):
	p = input()
	n = int(input())
	arr = eval(input())
	AC(p, arr)