import sys
input= sys.stdin.readline

for i in range(int(input())):
  n=int(input())
  x=[]
  for j in range(n):
    x.append(input().strip())
  x.sort()
  flag=True
  for i in range(n-1):
    if x[i] == x[i+1][0:len(x[i])]:
      flag = False
      break
  if flag:
    print("YES")
  else:
    print("NO")
