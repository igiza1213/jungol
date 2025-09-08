N = int(input())

arr = [0] * N


def condition(n):
    for i in range(1, n // 2 + 1):
        ls = n - i * 2
        rs = n - i
        if arr[ls : ls + i] == arr[rs : rs + i]:
            return 1
    return 0


def rep(c):
    if c == N:
        print(*arr, sep="")
        return 1
    for i in range(1, 4):
        arr[c] = i
        if condition(c + 1):
            continue

        ret = rep(c + 1)
        if ret:
            return 1
    return 0


rep(0)
