def solution(T):
    winter_max = T[0]
    summer_max = T[0]
    summer_cnt = 0
    for i in range(1, len(T)):
        if winter_max < T[i]:
            summer_cnt+=1
            summer_max = T[i] 
        else:
            summer_cnt=0
            winter_max = summer_max
    return len(T)-summer_cnt
# def solution(T):

#     if len(T)==0:
#         return 0

#     length = len(T)
#     winter_high = T[0]
#     total_high = T[0]
#     winter_len = 0

#     for t in T:
#         if t <= winter_high : 
#             winter_high = total_high
#         elif t > total_high :
#             overall_high = t

#     for t in T:
#         if t <= winter_high : 
#             winter_len += 1

#     return winter_len


print(solution([5, -2, 3, 8, 6]))
print(solution([-5, -5, -5, -42, 6, 12]))