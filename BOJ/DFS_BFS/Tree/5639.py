import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.val)


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


x = int(input())
root = Node(x)
while True:
    try:
        x = int(input())
    except:
        break
    cur = root 
    while True:
        if cur.val > x:
            if cur.left is None:
                cur.left = Node(x)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(x)
                break
            cur = cur.right

postorder(root)    