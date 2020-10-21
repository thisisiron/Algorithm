import sys 
input = sys.stdin.readline


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

a = []
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        a.append(temp)
b = {} 
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        if temp in b.keys():
            b[temp] += 1
        else:
            b[temp] = 1

result = 0
for i in a:
    if T - i in b.keys():
        result += b[T - i]
print(result)