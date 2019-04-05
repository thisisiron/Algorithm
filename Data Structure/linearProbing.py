TABLE_SIZE = 13

class element():
    key = ''

hash_table = [element() for _ in range(TABLE_SIZE)]

def transform(word):
    number = 0
    for key in word:
        number += ord(key)
    return number

def hash_function(word):
    return transform(word) % TABLE_SIZE

def empty(e):
    if len(e.key) == 0:
        return True

def equal(e1, e2):
    print(e1.key, e2.key)
    if e1.key == e2.key:
        return True

def hash_lp_add(item, hash_table):
    hash_value = i = 0
    hash_value = i = hash_function(item.key)
    while not empty(hash_table[i]):
        if equal(item, hash_table[i]):
            print("탐색키가 중복되었습니다.")
            return
        i = (i+1) % TABLE_SIZE
        if i==hash_value:
            print('테이블이 가득찼습니다.')
            return
    
    hash_table[i].key = item.key
    # hash_table[i] = item
    # 위 방식으로하면 해당 i번째에 element에 item(element)을 덧붙이기 때문에
    # hash_table[4] = item을 한다면
    # item값이 바뀌면 hash_table[4] 값도 바뀌게 된다. (얕은 복사)
    

def hash_lp_search(item, hash_table):
    i = hash_value = 0
    hash_value = i = hash_function(item.key)
    while not empty(hash_table[i]):
        if equal(item, hash_table[i]):
            print("탐색 성공 위치:", i)
            return
        i = (i+1) % TABLE_SIZE
        if i == hash_value:
            print('찾는 값이 테이블에 존재하지 않음.')
            return
    print("찾는 값이 없음.")


def hash_lp_print(hash_table):
    for item in hash_table:
        print("item key 출력: ",item.key)

if __name__ == "__main__":
    tmp = element()
    if tmp in hash_table:
        print("??")
    while True:
        op = input("원하는 연산을 선택(0=입력, 1=탐색, 2=종료) : ")
        if not op in ['0', '1', '2']:
            print("제대로 된 명령어를 입력해주세요")
            continue
        if op == '2':
            break
        tmp.key = input("키를 입력하세요 : ")
        if op == '0':
            hash_lp_add(tmp, hash_table)

        if op == '1':
            hash_lp_search(tmp, hash_table)

        hash_lp_print(hash_table)
        
# Hash Function Test
# d = 100, o = 111 -> 100 + 111 = 211 -> 211 % 13 = 3
# print("Hash Function Test",hash_function('do'))