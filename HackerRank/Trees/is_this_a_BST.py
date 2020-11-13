# link: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def isBST(tree, l=None, r=None):
    if tree == None:
        return True
    if l is not None and l.data >= tree.data:
        return False
    if r is not None and r.data <= tree.data:
        return False
    return isBST(tree.left, l, tree) and isBST(tree.right, tree, r)


def checkBST(root):
    check = isBST(root)
    return check 