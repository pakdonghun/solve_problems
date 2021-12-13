s = int(input())
x = 0
while s >=0:
    if s % 5 == 0:
        x += (s // 5)
        print(x)
        break
    s -= 3
    x += 1
else:
    print(-1)