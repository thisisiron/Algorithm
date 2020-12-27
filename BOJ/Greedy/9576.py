import sys
import bisect
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    books = []
    for _ in range(M):
        a, b = map(int, input().split())
        books.append((a, b))
    
    books.sort(key=lambda x: (x[0], x[1]))
    prev = 0
    ptr = 0
    cnt = 0
    while books:
        a, b = books.pop(0)
        
        if a > b:
           continue 

        if ptr < a:
            cnt += 1
            ptr = a
            while books:
                a, b = books.pop(0)
                if ptr == a:
                    bisect.insort(books, (a + 1, b))
                else:
                    bisect.insort(books, (a, b))
                    break
    print(cnt)