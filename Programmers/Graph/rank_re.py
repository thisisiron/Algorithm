def solution(n, results):
    answer = 0

    winers = {i:set() for i in range(n + 1)}
    losers = {i:set() for i in range(n + 1)}

    for res in results:
        winers[res[0]].add(res[1])
        losers[res[1]].add(res[0])
        
    for i in range(1, n + 1):
        for winer in losers[i]:
            winers[winer].update(winers[i])
        for loser in winers[i]:
            losers[loser].update(losers[i]) 

    for i in range(1, n + 1):
        if len(winers[i]) + len(losers[i]) == (n - 1):
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))