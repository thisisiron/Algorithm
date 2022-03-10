import sys
input = sys.stdin.readline


def score():
    global mn
    s_team = []
    l_team = []
    for i in range(N):
        if visited[i]:
            s_team.append(i)
        else:
            l_team.append(i)
    s_power = 0
    for i in range(len(s_team)):
        for j in range(i + 1, len(s_team)):
            s_power += (players[s_team[i]][s_team[j]] + players[s_team[j]][s_team[i]])
    
    l_power = 0
    for i in range(len(l_team)):
        for j in range(i + 1, len(l_team)):
            l_power += (players[l_team[i]][l_team[j]] + players[l_team[j]][l_team[i]])
            
    if mn > abs(s_power - l_power):
        mn = abs(s_power - l_power)
    return
    

def dfs(idx):
    if idx == N:
        score()
    else:
        visited[idx] = 1
        dfs(idx + 1)
        visited[idx] = 0
        dfs(idx + 1)


N = int(input())
players = [[int(x) for x in input().split()] for _ in range(N)]
visited = [0 for _ in range(N)]

mn = float('inf')
dfs(0)
print(mn)