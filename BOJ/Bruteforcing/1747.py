import sys
input = sys.stdin.readline

MAX = 1003002
N = int(input())
check = [0] * (MAX)

i = 2
while True:
    if check[i] == 0:
        for j in range(2 * i, MAX, i):
            check[j] = 1 
        if i >= N:
            if check[i] == 0 and str(i) == str(i)[::-1]:
                print(i)
                break
    i += 1