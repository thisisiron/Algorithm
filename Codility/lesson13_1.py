# This Solution didn't solve large number L => 62 point
# def solution(A, B):
#     result = [-1] * len(A)
#     for a in A:
#         if result[a-1] == -1:
#             result[a-1] = fibo(a)

#     return [result[a-1]%2**b for a,b in zip(A,B)]

# def fibo(N):
#     a = 0
#     b = 1
#     for i in range(N):
#         c = b + a
#         a = b
#         b = c    
#     return c

def solution(A, B):
    mx = max(A)
    B = [(1 << item) - 1 for item in B]
    fibo = [0] * (mx+2) 
    fibo[1] = 1
    for i in range(1, mx+1):
        fibo[i+1] = fibo[i] + fibo[i-1]
    result = [0] * len(A)
    for i in range(len(A)):
        result[i] = fibo[A[i]+1] & B[i]
    
    return result



#print(fibo(2))
print(solution([4,4,5,5,1], [3,2,4,3,1])) # [5, 1, 8, 0, 1]