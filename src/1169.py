N, M = map(int, input().split())
A = [0] * (N + 1)
used = [0] * 7

def recur(c):
    if c == N + 1:
        print(*A[1:])
        return

    for i in range(1, 7):
        if M == 2 and i < A[c - 1]:
            continue
        elif M == 3 and used[i]:
            
            continue
        # if M==3 and i in A[1:c]: continue
        A[c] = i
        used[i] = 1
        recur(c + 1)
        used[i] = 0


recur(1)
