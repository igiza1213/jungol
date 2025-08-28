n, m = map(int, input().split())
print(
    "\n".join(
        [
            " ".join(
                [
                    str((j + i * m) + (m + 1 - j * 2)) if i % 2 else str(j + i * m)
                    for j in range(1, m + 1)
                ]
            )
            for i in range(n)
        ]
    )
)
