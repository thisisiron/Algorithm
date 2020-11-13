# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    cnt = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            tmp = arr[i] 
            arr[i] = arr[tmp - 1]
            arr[tmp - 1] = tmp 
            cnt += 1
    return cnt