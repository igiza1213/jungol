t, n, k = map(int, input().split())

arr = []


def re_per():
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            arr.append(f"{i}{j}")

def per():
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if i == j:
                continue
            arr.append(f"{i}{j}")

if t == 1:
    re_per()
else:
    per()


for row in arr:
    print(*row)
