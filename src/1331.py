n = int(input())

matrix = [[0] * (n * 2 - 1) for _ in range(n * 2 - 1)]


dx, dy = [-1, 1, 1, -1], [1, 1, -1, -1]
c, o = 1, n - 1

while o > 0:
    x, y = n - 1, n - o - 1
    for f in range(4):

        for i in range(o):
            matrix[y][x] = c

            nx, ny = x + dx[f], y + dy[f]

            x, y = nx, ny
            c += 1

    o -= 1

matrix[n - 1][n - 1] = c


for row in matrix:
    print(*map(lambda v: " " if v == 0 else chr((v - 1) % 26 + ord("A")), row))
