n = int(input())


matrix = [[0] * n for _ in range(n)]

x, y = n // 2, 0

for i in range(1, n**2 + 1):
    matrix[y][x] = i

    if i % n:
        nx, ny = x - 1, y - 1
    else:
        nx, ny = x, y + 1

    x, y = nx % n, ny % n

for row in matrix:
    print(*row)
