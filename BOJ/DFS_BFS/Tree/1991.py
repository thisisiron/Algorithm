import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    print(node.val, end='')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)


def inorder(node):
    if node.left is not None:
        inorder(node.left)
    print(node.val, end='')
    if node.right is not None:
        inorder(node.right)


def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.val, end='')


if __name__ == '__main__':
    num_node: int = int(input())
    tree: dict = {}

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for a in alpha:
        tree[a] = Node(a, None, None)

    for i in range(num_node):
        val, l, r = input().split() 
        if l != '.':
            tree[val].left = tree[l]
        if r != '.':
            tree[val].right = tree[r]
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
