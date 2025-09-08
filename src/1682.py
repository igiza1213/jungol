N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

visit = [0] * N

res = 10000


def dfs(d, value, cur):
    global res
    if value >= res:
        return

    if d == N:
        if matrix[cur][0]:
            res = min(res, value + matrix[cur][0])
        return

    for i in range(1, N):
        if visit[i]:
            continue
        if matrix[cur][i] == 0:
            continue

        visit[i] = 1
        dfs(d + 1, value + matrix[cur][i], i)
        visit[i] = 0


dfs(1, 0, 0)

print(res)
