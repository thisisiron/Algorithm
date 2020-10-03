def solution(records: list) -> list:
    answer = []
    id_dict: dict = {}
    for row in records:
        data = row.split()
        if data[0] in ['Enter', 'Change']:
            ops, id, name = data
            if ops == 'Enter':
                answer.append((id, '님이 들어왔습니다.'))
                id_dict[id] = name
            elif ops == 'Change':
                id_dict[id] = name
        
        elif data[0] == 'Leave':
            ops, id = data
            answer.append((id, '님이 나갔습니다.'))
    answer = [id_dict[id] + x for id, x in answer]
    return answer


if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))