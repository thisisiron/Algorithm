def solution(jobs):
    answer, start = 0, 0
    jobs.sort(key=lambda x: x[1])
    num_jobs = len(jobs)

    while len(jobs):
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                print(jobs[i])
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                start += 1
    
    return answer // num_jobs 


print(solution([[0, 3], [1, 9], [2, 6]]))