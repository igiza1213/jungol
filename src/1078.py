from collections import deque

M, N = map(int, input().split())

matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

x, y = map(int, input().split())

y, x = y - 1, x - 1


dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(y, x, c):
    queue = deque([(y, x, c)])
    matrix[y][x] = c
    while queue:
        y, x, c = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or matrix[ny][nx] != 1:
                continue
            queue.append([ny, nx, c + 1])
            matrix[ny][nx] = c + 1

    return c

print(bfs(y, x, 3))

cnt = 0
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            cnt += 1

print(cnt)
    