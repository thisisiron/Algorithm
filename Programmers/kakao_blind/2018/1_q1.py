def solution(lines: list) -> int: 
    start_end: list = [] 
    for line in lines:
        _, res_time, pro_time = line.split()
        h: float
        m: float
        s: float
        h, m, s = map(float, res_time.split(':'))
        s += h * 3600 + m * 60
        s *= 1000
        pro_sec: float
        pro_msec: float
        splitted: list = pro_time[:-1].split('.')
        if len(splitted) == 1:
            pro_msec = float(splitted[0]) * 1000
        else:
            pro_sec, pro_msec = map(float, splitted)
            pro_msec += pro_sec * 1000
        start_end.append([s - pro_msec + 1 , s])

    answer: list = [] 
    for log_start, log_end in start_end:
        answer.append(check_throughput(log_start, start_end))
        answer.append(check_throughput(log_end, start_end))
    
    return max(answer)


def check_throughput(time: float, start_end: list) -> int:
    cnt: int = 0
    start: float = time
    end: float = time + 1000

    for cmp_start, cmp_end in start_end:
        if not (end <= cmp_start or start > cmp_end):
            cnt += 1 
    return cnt 
    

if __name__ == '__main__':
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))