n, m = map(int, input().split())

if n < 1 or n > 100 or m < 1 or m > 4 or not (n % 2):
    print("INPUT ERROR!")
else:
    if m == 1:
        for i in range(1, n + 1):
            print("*" * min(i, n - i + 1))
    elif m == 2:
        for i in range(1, n + 1):
            print(" " * max(n // 2 - i + 1, i - n // 2 - 1) + "*" * min(i, n - i + 1))
    elif m == 3:
        for i in range(1, n + 1):
            print(" " * min(i - 1, n - i) + "*" * max(i * 2 - n, n - (i * 2 - 2)))
    elif m == 4:
        for i in range(1, n + 1):
            print(
                " " * min(i - 1, n // 2) + "*" * max(n // 2 - i + 2, i - n + n // 2 + 1)
            )
