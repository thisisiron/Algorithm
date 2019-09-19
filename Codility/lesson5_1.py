def solution(A):
    # write your code in Python 3.6
    if A is None: return 0
    east = 0
    cnt = 0 
    for i, a in enumerate(A):
        if a == 0:
            east += 1
        elif a == 1:
            cnt += east
        
    if cnt <=  1000000000:
        return cnt
    else:
        return -1
