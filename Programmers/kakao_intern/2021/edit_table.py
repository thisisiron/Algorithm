# 정확성만 통과, 가장 기본적인 풀이법
def solution(n, k, cmd):
    arr = [1] * n
    stack = []
    cur = k
    
    for c in cmd:
        x = c.split()
        if len(x) == 1:
            if x[0] == 'C':
                arr[cur] = 0
                stack.append(cur)
                
                while cur < n - 1:
                    cur += 1
                    if arr[cur] == 1:
                        break
                
                if cur == n - 1:
                    while cur >= 0:
                        if arr[cur] == 1:
                            break
                        cur -= 1

            elif x[0] == 'Z':
                pre = stack.pop()
                arr[pre] = 1
                
        elif len(x) == 2:
            d, num = x
            num = int(num)
            while num:
                if d == 'U':
                    cur -= 1
                    if cur == -1:
                        cur = n - 1
                elif d == 'D':
                    cur += 1
                    cur %= n
                if arr[cur] == 1:
                        num -= 1
                        
    answer = ''.join(['O' if x == 1 else 'X' for x in arr])
    return answer