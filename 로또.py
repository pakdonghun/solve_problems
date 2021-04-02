import sys 
from itertools import combinations 

input = sys.stdin.readline 

while True: 
    lotto = list(input().split()) 
    if lotto[0] == '0': 
        break 
    for result in combinations(lotto[1:], 6): 
        print(' '.join(result))
    print()
