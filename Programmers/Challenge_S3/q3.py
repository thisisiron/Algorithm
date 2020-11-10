import sys
sys.setrecursionlimit(10**9)

sub_a = []


def subseq(a, b=[]):
    if len(a) == 0:
        if b:
            sub_a.append(b)
        return
    subseq(a[:-2], a[-2:] + b)
    subseq(a[:-2], b)
    return
    

def solution(a):
    answer = 0 
    for sub_a in a:

    subseq(a)
    sub_a.sort(key=lambda x: len(x), reverse=True)
    for arr in sub_a:
        if len(arr) <= 1:
            continue
        check = {arr[0], arr[1]}
        for i in range(0, len(arr), 2):
            print(arr, i, ":", arr[i], arr[i + 1])
            if arr[i] == arr[i + 1]:
                check = {}
                break
            check &= {arr[i], arr[i + 1]}
            if len(check) == 0:
                break
        if len(check) >= 1:
            answer = len(arr)
            break
    return answer


print(solution([0]))
print(solution([0, 2]))
print(solution([5,2,3,3,5,3]))
print(solution([5,2,3,3,5,3,4]))
print(solution([0,3,3,0,7,2,0,2,2,0]))