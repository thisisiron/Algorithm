# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def traversal(root, result):
    if root is None:
        return len(result)
    else:
        result.add(root.x)
        a = traversal(root.l, result.copy())
        b = traversal(root.r, result.copy())
        
        if a > b:
            return a
        else:
            return b

def solution(T):
    if T==None:
        return 0
    result = set()    
    c = traversal(T, result)
    return c
        