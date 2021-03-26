n = int(input())
score = []
answer = 0

for i in range(n):
    score.append(int(input()))

score = score[::-1]

for i in range(1,n):
    if score[i-1] <= score[i]:
        x = (score[i] - score[i-1] + 1)
        score[i] -= x
        answer +=x

print(answer)
