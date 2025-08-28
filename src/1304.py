print(
    (
        lambda n: "\n".join(
            [
                " ".join(map(str, list(range(1 + i, n**2 - n + 2 + i, n))))
                for i in range(n)
            ]
        )
    )(int(input()))
)
