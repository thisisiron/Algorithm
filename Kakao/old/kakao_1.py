def solution(record):
    answer = []
    cmd = []
    uid = dict()
    
    for row in record:
        cmd.append([row.split()[0], row.split()[1]])
        if cmd[-1][0] != 'Leave':
            uid[row.split()[1]] = row.split()[2]
    for c in cmd:
        if c[0]=="Enter":
            answer.append(uid[c[1]]+"님이 들어왔습니다.")
        elif c[0]=="Leave":
            answer.append(uid[c[1]]+"님이 나갔습니다.")
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])