def solution(S, P, Q):
    # write your code in Python 3.6
    M = len(P)
    x_list = [[0,0,0,0]]
    counter = [0] * 4
    for s in S:
        if s == 'A':
            counter[0] += 1
            x_list.append(counter[:])
        elif s == 'C':
            counter[1] += 1
            x_list.append(counter[:])
        elif s == 'G':
            counter[2] += 1
            x_list.append(counter[:])
        elif s == 'T':
            counter[3] += 1
            x_list.append(counter[:])
    
    
    answer = []
    for i in range(M):
        for j in range(4):
            val = x_list[Q[i]+1][j] - x_list[P[i]][j]
            if val != 0:
                answer.append(j+1)
                break
        
    return answer
