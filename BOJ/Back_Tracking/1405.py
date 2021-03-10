import sys
input = sys.stdin.readline


def dfs(y, x, cnt, prob, visited):
    global res 

    if cnt == num:
        res += prob
        
    else:
        visited[(y, x)] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny, nx) in visited and visited[(ny, nx)] == True:
                continue
            dfs(ny, nx, cnt + 1, prob * p[i], visited)
        visited[(y, x)] = False 

num, E, W, S, N = map(int, input().split())
p = [E/100, W/100, S/100, N/100]
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
visited = {}
res = 0

dfs(0, 0, 0, 1, visited)
print(res)