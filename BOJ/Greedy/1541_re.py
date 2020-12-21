import sys
input = sys.stdin.readline


formula = input().split('-')

s = 0
for i in formula[0].split('+'):
    s += int(i)
for i in formula[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)