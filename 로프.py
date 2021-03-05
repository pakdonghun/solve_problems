n = int(input())
rope = []

for i in range(n):
    ropes=int(input())
    rope.append(ropes)

rope.sort(reverse=True)

w = 0
for i in range(n):
    if w<rope[i]*(i+1):
        w=rope[i]*(i+1)
print(w)
