n = int(input())

matrix = [[0] * n for i in range(n)]

dx, dy = [0, 1, 1, -1], [1, -1, 0, 1]
x, y, f, c = 0, 0, 0, 1

while c <= n**2:
    matrix[y][x] = c

    nx, ny = x + dx[f], y + dy[f]

    if (
        (f == 1 and (0 >= ny or n - 1 == nx))
        or (f == 3 and (0 >= nx or n - 1 == ny))
        or (f == 0)
        or (f == 2)
    ):
        f = (f + 1) % 4

    if ny >= n:
        nx, ny = x + 1, y
    if nx >= n:
        nx, ny = x, y + 1

    x, y = nx, ny

    c += 1

for row in matrix:
    print(" ".join(map(str, row)))
