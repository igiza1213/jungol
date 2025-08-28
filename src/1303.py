print()(
    lambda n, m: "\n".join(
        [" ".join([str(j + i * m) for j in range(1, m + 1)]) for i in range(n)]
    )
)(*map(int, input().split()))
