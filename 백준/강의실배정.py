import sys
import heapq
heap=[]
input = sys.stdin.readline
N = int(input())
time=[]
for i in range(N):
    start, end = map(int, input().split())
    time.append([start,end])

time.sort(key=lambda x:x[0])
heapq.heappush(heap, time[0][1])
for i in range(1,N):
    if heap[0] > time[i][0]:
        heapq.heappush(heap, time[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])
print(len(heap))
