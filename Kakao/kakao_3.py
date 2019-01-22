def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    
    candi = []
    for j in range(col):
        for i in range(row):
            candi.append(relation[i][j])
        if len(set(candi)) == row:
            answer+=1


    return answer

print(solution([['100','ryan','music','2'],['200','apeach','math','2'],['300','tube','computer','3'],['400','con','computer','4'],['500','muzi','music','3'],['600','apeach','music','2']]))