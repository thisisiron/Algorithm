def solution(n, computers):
    answer = 0
    visited = {}
    
    for i, total_n in enumerate(computers):
        if i not in visited:
            network = []
            visited[i] = True
            network.append(i)
            for nextCom in network:
                for j,computer in enumerate(computers[nextCom]):
                    if computer == 1 and j not in visited:
                        print("i:", i, " j:", j, " computer:", computer)
                        network.append(j)
                        visited[j] = True
            answer+=1

            
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))