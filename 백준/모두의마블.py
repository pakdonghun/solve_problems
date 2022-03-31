import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
A.sort(reverse=True)

answer = 0

for i in range(len(A)):
    if i <= 1:
        answer += A[i]
    else:
        answer += A[0] + A[i]

print(answer)
