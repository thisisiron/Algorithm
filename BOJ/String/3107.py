import sys
input = sys.stdin.readline


ip = input().rstrip().split(':')

if len(ip) == 8:
	print(":".join([f"{x.zfill(4)}" for x in ip]))
else:
	idx = 0
	flag = False
	ans = ['' for _ in range(8)] 

	for i in range(len(ip)):

		if len(ip[i]) == 4:
			ans[idx] = ip[i]
			idx += 1
		elif len(ip[i]) > 0:
			ans[idx] = ip[i].zfill(4)
			idx += 1
		else:
			if not flag:
				for j in range(8 - len(ip) + 1):
					ans[idx] = '0000'
					idx += 1
				flag = True
			else:
				ans[idx] = '0000'
				idx += 1

	print(':'.join(ans))