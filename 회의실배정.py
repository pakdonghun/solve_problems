import sys
input = sys.stdin.readline
time=[]
N = int(input())

for i in range(N):
    start, end = map(int, input().split())
    time.append([start,end])

time.sort(key=lambda x:(x[1],x[0]))

last = 0
count = 0

for i,j in time:
    if i >= last:
        count +=1
        last = j
print(count)
