def solution(n, costs):
    answer = 0

    root = list(range(0, n)) 
    costs.sort(key=lambda x: x[2])
    for u, v, c in costs:
        x = find(root, u)
        y = find(root, v)
        if x != y:
            union(root, x, y)
            answer += c

    return answer


def union(root, x, y):
    x = find(root, x)
    y = find(root, y)
    root[y] = x


def find(root, x):
    if root[x] == x:
        return x
    else:
        return find(root, root[x])


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))