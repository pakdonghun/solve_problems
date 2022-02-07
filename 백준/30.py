a = list(input())
a.sort(reverse = True)
sum = 0
for _ in a:
    sum += int(_)
if sum % 3 != 0 or '0' not in a:
    print(-1)
else:
    print(''.join(a),end = '')
