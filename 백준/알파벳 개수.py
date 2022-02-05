s = [0]*26

for i in input():
    s[ord(i)-ord('a')] += 1
print(*s)
