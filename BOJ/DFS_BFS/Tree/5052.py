import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.check = False


class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def add(self, number: str):
        cur = self.head
        for nu in number:
            if nu not in cur.child:
                cur.child[nu] = Node(nu)
            cur = cur.child[nu]
            if cur.check == True:
                return False
        cur.check = True

        return True
    

def main():
    t = int(input())
    for _ in range(t):

        n = int(input())
        check = True 

        trie = Trie()
        phone_list = []
        for _ in range(n):
            phone_list.append(input().rstrip())
    
        phone_list.sort(key=lambda x: len(x))

        for phone_number in phone_list:
            check = trie.add(phone_number)
            if not check:
                break
        if check:
            print('YES')
        else:
            print('NO')



if __name__ == '__main__':
    main()
