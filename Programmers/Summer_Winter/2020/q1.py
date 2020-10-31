def solution(n, delivery):
    check = {i: '?' for i in range(1, n + 1)}
    delivery.sort(key=lambda x: x[2], reverse=True)
    
    for b1, b2, d in delivery:
        if d == 1:
            check[b1] = 'O'
            check[b2] = 'O'
        elif d == 0:
            if check[b1] == 'O':
                check[b2] = 'X'
            elif check[b2] == 'O':
                check[b1] = 'X'

    return ''.join([check[i] for i in range(1, n + 1)])


print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))