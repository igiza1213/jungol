N, M = map(int, input().split())

arr = [0] * (N + 1)


def recur(c):
    if c == N + 1:
        if sum(arr) == M:
            print(*arr[1:])
        return
    for i in range(1, 7):
        arr[c] = i
        recur(c + 1)


recur(1)
