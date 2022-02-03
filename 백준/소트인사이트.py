n = int(input())
a = list(map(int,str(n)))

a.sort(reverse=True)
for i in a:
    print(i,end='')
