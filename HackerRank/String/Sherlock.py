# link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings


# Complete the isValid function below.
def isValid(s):
    from collections import Counter
    s_counter = Counter(s)
    char, freq = list(s_counter.keys()), list(s_counter.values())
    chance = 1    
    pre_c, pre_f = char[0], freq[0]
    for c, f in zip(char[1:], freq[1:]):
        if pre_f != f:
            if chance:
                chance -= 1
            else:
                return 'NO'
            
    return 'YES'