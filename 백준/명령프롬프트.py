s = int(input())
a = list(input())
n = len(a)

for _ in range(s - 1):
    b = list(input())
    for i in range(n):
        if a[i] != b[i]:
            a[i] = '?'
print(''.join(a))
