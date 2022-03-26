import sys
input = sys.stdin.readline

N = input()
P = list(map(int, input().split()))
P.sort()

sum = 0
new = 0
for i in P:
    new += i
    sum += new
print(sum)
