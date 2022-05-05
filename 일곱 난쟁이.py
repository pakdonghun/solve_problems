import sys

input = sys.stdin.readline

nan = [int(input) for _ in range(9)]

answer = sum(nan)

a = 0
b = 0

for i in range(9):
    for j in range(9):
        if answer - (nan[i]+nan[j]) == 100:
            a,b = nan[i],nan[j]
            break

nan.remove(a)
nan.remove(b)
nan.sort()

for i in nan:
    print(i)
