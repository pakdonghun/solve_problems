import sys

x = int(input())
answer = sys.stdin.readline().split()

y = []

for i in range(x):
    y.append(" ".join(answer[::2]))
    answer = answer[1::2]

for a in y[::-1]:
    print(a)
