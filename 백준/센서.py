import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

sensor = sorted(list(map(int, input().split())))

array = []

if K >= N:
    print(0)


for i in range(1,N):
    array.append(sensor[i]-sensor[i-1])

array.sort()

print(sum(array[:N-K]))
    

