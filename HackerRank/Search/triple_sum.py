#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    cnt = {}
    for q in b:
        for p in a:
            if p <= q:
                for r in c:
                    if q >= r:
                        # print(p, q, r)
                        cnt.setdefault((p, q, r), 0)
                        cnt[(p, q, r)] +=1
        
    return len(cnt.values())
                

if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        lines = file.readlines()

    lenaLenbLenc = lines[0].split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, lines[1].rstrip().split()))
    arrb = list(map(int, lines[2].rstrip().split()))
    arrc = list(map(int, lines[3].rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    print(ans)  # 9593177511025 