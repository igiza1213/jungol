t, n, k = map(int, input().split())

arr = []


def re_com():
    for i in range(1, k + 1):
        for j in range(i, k + 1):
            arr.append(f"{i}{j}")


def com():
    for i in range(1, k + 1):
        for j in range(i, k + 1):
            if i == j:
                continue
            arr.append(f"{i}{j}")


if t == 1:
    re_com()
else:
    com()


for row in arr:
    print(*row)
