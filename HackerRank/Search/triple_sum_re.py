def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    idx_a, idx_c = 0, 0
    cnt = 0
    for q in b:
        while idx_a < len(a):
            if a[idx_a] <= q:
                idx_a += 1
            else:
                break

        while idx_c < len(c):
            if c[idx_c] <= q:
                idx_c += 1
            else:
                break
                
        cnt += idx_a * idx_c
    return cn