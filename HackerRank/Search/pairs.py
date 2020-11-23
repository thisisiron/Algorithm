# Complete the pairs function below.
def pairs(k, arr):
    cnt = 0
    check = set(arr)
    for a in arr:
        if a - k in check:
            cnt += 1
    return cnt