import sys
input = sys.stdin.readline


C = int(input())
for c in range(C):
    N, *score =  map(int, input().split())
    m = sum(score) / N
    print(f'{sum([1 for x in score if x > m]) / N * 100:.3f}%')