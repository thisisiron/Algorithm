import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def split(preorder, inorder):
	global ans
	if len(preorder) == 0:
		return
	if len(preorder) == 1:
		ans += preorder
		return

	root = preorder[0]
	root_idx = inorder.index(root)
	split(preorder[1:root_idx + 1], inorder[:root_idx])
	split(preorder[root_idx + 1:], inorder[root_idx + 1:])
	ans.append(root)


T = int(input())

for _ in range(T):
	n = int(input())
	preorder = input().rstrip().split()
	inorder = input().rstrip().split()
	ans = []

	split(preorder, inorder)
	print(*ans)