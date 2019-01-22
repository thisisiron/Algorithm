uni = set()

def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    visited = [0 for _ in range(col)]    
    for k in range(1,col+1):
        back(col,k,visited)
    uni_list = list(uni)
    uni_list.sort(key=lambda x: len(x))
    
    for idx,k in enumerate(uni_list):
        candi = set()
        for i in range(row):
            result = []
            for j in k:
                result.append(relation[i][j])
            candi.add(tuple(result))
            if len(candi)<i+1:
                break
                    
            if len(candi) == row:
                uni_copy = uni_list[idx+1:].copy()
                for x in uni_copy:
                    if set(x) & set(k)==set(k):
                        uni_list.remove(x)
                answer+=1
    return answer


def back(n,k,visited):
    if n==k:
        return
    else:
        combi = []
        for x in range(n):
            if visited[x]!=1:
                visited[x]=1
                combi.append(x)
                uni.add(tuple(combi))
                back(n, x+1,visited)
                visited[x]=0

print(solution([['100','ryan','music','2'],['200','apeach','math','2'],['300','tube','computer','3'],['400','con','computer','4'],['500','muzi','music','3'],['600','apeach','music','2']]))