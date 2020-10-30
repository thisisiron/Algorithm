def solution(cookie):
    mx = 0
    for mid in range(0, len(cookie) - 1):
        first = cookie[mid]
        second = cookie[mid + 1]
        left = mid
        right = mid + 1
        
        while True:
            if first == second:
                if mx < first:
                    mx = first
            
            if first <= second and 0 < left:
                left -= 1
                first += cookie[left]
            elif first >= second and right < len(cookie) - 1:
                right += 1
                second += cookie[right]
            else:
                break
        
    return mx 

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))