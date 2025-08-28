n = int(input())

if n < 1 or n > 100 or not (n % 2):
    print("INPUT ERROR!")
else:
    for i in range(1, n + 1):
        print(" " * min(i - 1, n - i) + "*" * min(i * 2 - 1, n * 2 - (i * 2 - 1)))
