def fact(n: int) -> int:
    if n == 1:
        print("1! = 1")
        return 1
    else:
        print(f"{n}! = {n} * {n-1}!")
        return n * fact(n - 1)


print(fact(int(input())))
