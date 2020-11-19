# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    counter = {}
    ans = 0
    
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            chunk = ''.join(sorted(s[j:j + i]))
            ans += counter.setdefault(chunk, 0)
            counter[chunk] += 1
    return an