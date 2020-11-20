# Complete the minimumBribes function below.
def minimumBribes(q):
    cnt = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            cnt = 0
            break
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                cnt += 1
    print(cnt if cnt != 0 else 'Too chaotic')