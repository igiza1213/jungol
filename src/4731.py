import sys

w, h = map(int, input().split())

matrix = [list(sys.stdin.readline().strip()) for i in range(h)]

flag = int(input())


def rotate_90(mat):
    return [list(row) for row in zip(*mat[::-1])]


def rotate_180(mat):
    return [row[::-1] for row in mat[::-1]]


def rotate_270(mat):
    return [list(row) for row in zip(*mat)][::-1]


def flip_h(mat):
    return mat[::-1]


def flip_v(mat):
    return [row[::-1] for row in mat]


if flag == 0:
    matrix = rotate_90(matrix)
elif flag == 1:
    matrix = rotate_180(matrix)
elif flag == 2:
    matrix = rotate_270(matrix)
elif flag == 3:
    matrix = flip_h(matrix)
elif flag == 4:
    matrix = flip_v(matrix)

print(len(matrix[0]), len(matrix))

for row in matrix:
    print("".join(row))
