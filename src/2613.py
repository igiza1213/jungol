from collections import deque

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(y, x, arr):
    v = 0
    queue = deque([*arr])
    while queue:
        y, x, v = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not matrix[ny][nx]:
                queue.append([ny, nx, v + 1])
                matrix[ny][nx] = v + 1

    return v


def proc():
    arr = []
    res = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                arr.append([y, x, 0])
    res = max(res, bfs(y, x, arr))

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 0:
                print(-1)
                return

    print(res)


proc()
