import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
    if A[i] in plugs:
        continue

    if len(plugs) < N:
        plugs.append(A[i])
        continue

    A_idxs = []
    hasplug = True

    for j in range(N):
        if plugs[j] in A[i:]:
            A_idx = A[i:].index(plugs[j])
        else:
            A_idx = 101
            hasplug = False

        A_idxs.append(A_idx)

        if not hasplug:
            break

    A_out = A_idxs.index(max(A_idxs))
    del plugs[A_out]
    plugs.append(A[i])
    count += 1

print(count)
