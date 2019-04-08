def solution(N):
    x = bin(N)[2:]
    return len(max(x.strip('0').strip('1').split('1')))