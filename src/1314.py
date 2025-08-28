n, m = map(int, input().split())

if n < 1 or n > 100 or m < 1 or m > 3:
    print("INPUT ERROR!")
else:
    if m == 3:
        for i in range(n):
            print(" " * (n - i - 1) + "*" * (2 * (i + 1) - 1))
    else:
        for i in range(n):
            op = (i + 1) if m % 2 else n - i
            print("*" * op)
