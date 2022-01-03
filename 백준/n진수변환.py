def solution(n, k):
    base = ''
 
    while n > 0:
        n, mod = divmod(n,k)
        base += str(mod)
    
    return base[::-1]
print(solution(124124,2))
