import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def postorder(arr, start, end):
    if start > end:
        return
    
    div = end + 1
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            div = i
            break
    postorder(arr, start + 1, div - 1)
    postorder(arr, div, end)
    print(arr[start])


answer = []
while True:
    try:
        x = int(input())
    except:
        break
    answer.append(x)
postorder(answer, 0, len(answer) - 1)