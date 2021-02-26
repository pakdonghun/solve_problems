from math import gcd 
def solution(w,h):
    answer = 1
    a  = gcd(w,h)
    answer = w*h - (w+h-a)
    return answer
