n = int(input())

for i in range(n):
    count = 0
    sum = 0
    a = list(input())
    for j in a:
        if j == 'O':
            count +=1
            sum = sum+count
        else:
            count = 0
    print(sum)
