n = int(input())

matrix = [[-1] * i for i in range(1, n + 1)]

dx, dy = [1, -1, 0], [1, 0, -1]

x, y, f, c = 0, 0, 0, 0

for j in range(1, n * (n + 1) // 2 + 1):
    matrix[y][x] = c

    nx, ny = x + dx[f], y + dy[f]

    if nx > j or nx < 0 or ny >= n or ny < 0 or matrix[ny][nx] != -1:
        f = (f + 1) % 3
        nx, ny = x + dx[f], y + dy[f]

    x, y = nx, ny

    c = (c + 1) % 10

for row in matrix:
    print(" ".join(map(str, row)))
49
