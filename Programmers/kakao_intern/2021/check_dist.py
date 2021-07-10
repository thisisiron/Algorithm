from collections import deque


N = None


def solution(places):
    global N

    N = 5
    answer = []
    
    for place in places:
        is_ok = True
        for i in range(N):
            for j in range(N):
                if place[i][j] == 'P':
                    is_ok = bfs(place, i, j)
                    
                    if not is_ok:
                        break
                        
            if not is_ok:
                break
                
        if is_ok:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer


dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)


def bfs(place, y, x):
    q = deque()
    q.append((y, x, 0))
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    is_ok = True
    
    while q:
        y, x, dist = q.popleft()
        
        if dist >= 2:
            break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            
            if place[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, dist + 1))
                    visited[ny][nx] = 1

                    if place[ny][nx] == 'P':
                        is_ok = False
    return is_ok