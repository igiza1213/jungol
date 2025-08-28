n, m = map(int, input().split())

dp = [[-1] * i for i in range(1, n + 1)]

x, y, value = 0, 0, 0

for _ in range(n * (n + 1) // 2):

    if y - 1 < 0 or x - 1 < 0 or x >= len(dp[y - 1]):
        value = 1
    else:
        value = dp[y - 1][x - 1] + dp[y - 1][x]

    dp[y][x] = value

    if x >= y:
        x = 0
        y += 1
    else:
        x += 1

if m == 1:
    for row in dp:
        print(" ".join(map(str, row)))
elif m == 2:
    for i, row in enumerate(dp[::-1]):
        print(" " * i + " ".join(map(str, row)))
elif m == 3:
    rev = dp[::-1]
    for i in range(len(rev)):
        for j in range(i, -1,-1):
            print(rev[i-j][j], end=" ")
        print()
