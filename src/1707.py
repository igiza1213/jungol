n = int(input())

matrix = [[0] * n for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y, f = 0, 0, 0

for i in range(1, n**2 + 1):
    matrix[y][x] = i

    nx, ny = x + dx[f], y + dy[f]

    if nx >= n or nx < 0 or ny >= n or ny < 0 or matrix[ny][nx]:
        f = (f + 1) % 4
        nx, ny = x + dx[f], y + dy[f]

    x, y = nx, ny

for row in matrix:
    print(" ".join(map(str, row)))
