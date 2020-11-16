from itertools import permutations


def solution(user_ids, banned_ids):
    bad_users = []
    for candi_users in permutations(user_ids, len(banned_ids)):
        if check(candi_users, banned_ids):
            candi_users = set(candi_users)
            if candi_users not in bad_users:
                bad_users.append(candi_users)
    return len(bad_users)


def check(candi_ids, banned_ids):
    for i in range(len(banned_ids)):
        if len(candi_ids[i]) != len(banned_ids[i]):  # ban된 id의 길이와 후보 id의 길이가 다른 경우
            return False
        if not match_id(candi_ids[i], banned_ids[i]):  # 후보 id가 ban된 id와 매칭되는지 확인 
            return False
    return True


def match_id(candi_id, banned_id):
    for i in range(len(candi_id)):
        if banned_id[i] == '*':
            continue
        elif candi_id[i] != banned_id[i]:
            return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))