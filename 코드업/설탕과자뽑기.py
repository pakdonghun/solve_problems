a,b = map(int,input().split())
zero = [[0 for j in range(a+1)] for i in range(b+1)]

c = int(input())
for i in range(c):
    d,f,x,y = map(int, input().split())
    for j in range(d):
        if f == 0:
            zero[x][y+j]=1
        else:
            zero[x+j][y]=1

for i in range(1,a+1):
    for j in range(1,b+1):
        print(zero[i][j],end=' ')
    print()
