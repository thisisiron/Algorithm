import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    books = []
    check = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        books.append((b, a))
    
    books.sort()
    
    for b, a in books:
        for i in range(a, b + 1):
            if check[i] == 0:
                check[i] = 1
                break
    print(sum(check))