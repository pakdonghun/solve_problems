import sys

for i in range(int(sys.stdin.readline())):
    P = list(sys.stdin.readline())
    N = len(P)
    nums = int(sys.stdin.readline())
    X = list(sys.stdin.readline()[1:-1].split(','))
    for j in P:
        try:
            if j == 'R':
                X.reverse()
            elif j == 'D':
                del X[0]
                nums -=1
        except:
            sys.stdout.write('error\n')
            break
    for i in range(nums):
        if i==0:
            sys.stdout.write('[')
        if i != (nums-1):
            sys.stdout.write(X[i]+',')
        else:
            sys.stdout.write(X[i]+']')
