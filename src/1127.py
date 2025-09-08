n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

m = 1000000000


def rep(k, s, b, pre):
    global m
    if k:
        m = min(m, abs(s - b))
    if k == n:
        return
    for i in range(pre + 1, n):
        rep(k + 1, s * arr[i][0], b + arr[i][1], i)


rep(0, 1, 0, -1)

print(m)
