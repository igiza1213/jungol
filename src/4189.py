from collections import deque

N, M = map(int, input().split())
r, c, s, k = map(int, input().split())

matrix = [[-1] * M for _ in range(N)]

dx, dy = [2, 1, -1, -2, -2, -1, 1, 2], [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    matrix[r - 1][c - 1] = 0
    matrix[s - 1][k - 1] = -2
    queue = deque([(r - 1, c - 1, 0)])

    while queue:
        y, x, v = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if matrix[ny][nx] == -2:
                print(v+1)
                return
            if matrix[ny][nx] != -1:
                continue
            queue.append([ny, nx, v + 1])
            matrix[ny][nx] = v + 1


bfs()
