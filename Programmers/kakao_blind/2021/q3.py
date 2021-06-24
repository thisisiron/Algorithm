def solution(n, s, a, b, fares):
    answer = float('inf')
    
    roads = [[float('inf')] * n for _ in range(n)]
        
    for u, v, c in fares:
        roads[u - 1][v - 1] = c
        roads[v - 1][u - 1] = c
    
    for i in range(n):
        roads[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                roads[j][k] = roads[j][i] + roads[i][k] if roads[j][k] > roads[j][i] + roads[i][k] else roads[j][k]
    s -= 1  
    a -= 1
    b -= 1
    
    for i in range(n):
        answer = answer if answer < roads[s][i] + roads[i][a] + roads[i][b] else roads[s][i] + roads[i][a] + roads[i][b]
    
    return answer