import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        phone_list = []
        for _ in range(n):
            phone_list.append(input().rstrip())
        
        phone_list.sort()
        cmp_phone = phone_list[0]
        check = True
        for phone in phone_list[1:]:
            if phone.startswith(cmp_phone):
                check = False
                break
            else:
                cmp_phone = phone

        print('YES' if check else 'NO')


if __name__ == '__main__':
    main()