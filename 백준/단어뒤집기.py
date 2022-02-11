import sys
s = int(input())

for _ in range(s):
    str = sys.stdin.readline().rstrip()
    word = list(str.split())
    reverse_word = []

    for i in word:
        reverse_word.append(i[::-1])

    x = " ".join(reverse_word)
    print(x)

