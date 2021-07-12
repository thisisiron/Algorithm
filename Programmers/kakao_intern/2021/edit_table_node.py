class Node:
    def __init__(self, idx, x, pre=None, nxt=None):
        self.x = x
        self.pre = pre
        self.nxt = nxt
        self.idx = idx


def solution(n, k, cmd):
    answer = ''
    
    linked = []
    pre = Node(0, 1, None, None)
    linked.append(pre)
    s = pre
    for i in range(1, n):
        cur = Node(i, 1, pre, None)
        linked.append(cur)
        pre.nxt = cur
        pre = cur
        if i == k:
            ptr = cur
    
    stack = []
    
    for c in cmd:
        if len(c) == 1:
            if c == 'C':
                stack.append((ptr, ptr.pre, ptr.nxt))
                ptr.x = 0
                if ptr.pre is not None:
                    ptr.pre.nxt = ptr.nxt
                if ptr.nxt is not None:
                    ptr.nxt.pre = ptr.pre
                ptr = ptr.nxt if ptr.nxt is not None else ptr.pre
            elif c == 'Z':
                removed, pre_removed, nxt_removed = stack.pop()
                if pre_removed is not None:
                    pre_removed.nxt = removed
                removed.pre = pre_removed
                if nxt_removed is not None:
                    nxt_removed.pre = removed
                removed.nxt = nxt_removed
                removed.x = 1
                
        else:
            d, num = c.split()
            num = int(num)
            for _ in range(num):
                if d == 'U':
                    ptr = ptr.pre
                elif d == 'D':
                    ptr = ptr.nxt
        
    
    for a in linked:
        if a.x == 1:
            answer += 'O'
        else:
            answer += 'X'
        
    return answer


if __name__ == '__main__':
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))