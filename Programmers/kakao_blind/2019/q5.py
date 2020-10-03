import sys


sys.setrecursionlimit(10**6)

def solution(nodeinfo: list) -> list:
    answer: list = [[], []]
    temp: list = [(pos, val) for val, pos in enumerate(nodeinfo, 1)]
    temp.sort(key=lambda x: (x[0][1], -x[0][0]), reverse=True)
    nodeinfo, indexinfo = zip(*temp)

    head: Node = Node(indexinfo[0], *nodeinfo[0]) 

    for (x, y), val in zip(nodeinfo[1:], indexinfo[1:]):
        cur: Node = head
        while True:
            if x < cur.x:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left = Node(val, x, y)
                    break
            else:
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    cur.right = Node(val, x, y) 
                    break
            break
        
    preorder(head, answer)
    postorder(head, answer)
        
    return answer


class Node(object):
    def __init__(self, data: int, x: int, y: int):
        self.data: int = data
        self.x: int = x
        self.y: int = y
        self.left: Node = None
        self.right: Node = None


def preorder(node: Node, answer: list):
    answer[0].append(node.data)
    if node.left:
        preorder(node.left, answer)
    if node.right:
        preorder(node.right, answer)


def postorder(node: Node, answer: list):
    if node.left:
        postorder(node.left, answer)
    if node.right:
        postorder(node.right, answer)
    answer[1].append(node.data)


if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))  # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]