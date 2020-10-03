from collections import Counter
def solution(N, stages):
    answer = []
    person = len(stages)
    st = Counter(stages)
    for i in range(1,N+1):
        k = st[i]
        if person==0: 
            answer.append([0,i])
        else:
            answer.append([k / person, i])
            person -= k
    answer.sort(key=lambda l:l[0], reverse=True)
    return [x[1] for x in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(3, [2,2,2,2]))