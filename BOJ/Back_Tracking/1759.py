import sys
input = sys.stdin.readline


vowel = ['a', 'e', 'i', 'o', 'u']

def gene_pw(candi, start, n_v, n_c):
    if len(candi) == L:
        if candi not in ans and  n_v >= 1 and n_c >= 2:
            ans.append(candi)
    else:
        for i in range(start, C):
            if alphas[i] not in candi:
                candi += alphas[i]
                if alphas[i] in vowel:
                    n_v += 1
                else:
                    n_c += 1
                gene_pw(candi, i + 1, n_v, n_c)

                candi = candi[:-1]
                if alphas[i] in vowel:
                    n_v -= 1
                else:
                    n_c -= 1


L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()
ans = []
gene_pw('', 0, 0, 0)
print(*ans, sep='\n')