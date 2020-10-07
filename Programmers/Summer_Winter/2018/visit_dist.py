def solution(dirs):
    cur = (0, 0)    
    visited = set() 

    for d in dirs:
        if d == 'U':
            nxt = (cur[0] + 1, cur[1])
        elif d == 'D':
            nxt = (cur[0] - 1, cur[1])
        elif d == 'L':
            nxt = (cur[0], cur[1] - 1)
        elif d == 'R':
            nxt = (cur[0], cur[1] + 1)
        if -5 <= nxt[0] <= 5 and -5 <= nxt[1] <= 5:
            visited.add((cur[0], cur[1], nxt[0], nxt[1]))
            visited.add((nxt[0], nxt[1], cur[0], cur[1]))
            cur = nxt
    return len(visited) // 2 


print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))