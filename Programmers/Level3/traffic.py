def solution(lines): 
    start_end = []
    for line in lines:
        _, res_time, ps = line.split()
        h, m, s = map(float, res_time.split(':'))
        s += (h * 3600) + (m * 60)
        ps = float(ps[:-1])
        start_end.append((s - ps + .001, s))
    
    answer = []
    for s, e in start_end:
        answer.append(check(s, start_end))
        answer.append(check(e, start_end))
        
        
    return max(answer)
   

def check(time, logs):
    cnt = 0
    s = time
    e = time + 1
    for log_s, log_e in logs:
        if not (e <= log_s or s > log_e):
            cnt += 1
    return cnt