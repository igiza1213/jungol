import sys


def rotate_90(mat):
    # 시계 방향 90도 회전
    return [list(row) for row in zip(*mat[::-1])]


def rotate_180(mat):
    # 180도 회전 : 위·아래 뒤집고, 각 행도 뒤집는다
    return [row[::-1] for row in mat[::-1]]


def rotate_270(mat):
    # 시계 방향 270도 회전
    # 90도 회전을 3번 하면 되지만, 바로 구현
    return [list(row) for row in zip(*mat)][::-1]


def rotate_360(mat):
    # 360도 회전 = 원본 그대로
    return mat


def print_matrix(mat):
    out = "\n".join(" ".join(map(str, row)) for row in mat)
    sys.stdout.write(out + "\n")


def solve() -> None:
    input = sys.stdin.readline

    n = int(input().strip())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    VALID = {90, 180, 270, 360}

    while True:
        line = input()
        if not line:  # EOF
            break
        angle = int(line.strip())

        if angle == 0:  # 종료
            break

        # 잘못된 각도이면 다시 입력받는다
        while angle not in VALID:
            angle = int(input().strip())

        # 회전 수행
        if angle == 90:
            matrix = rotate_90(matrix)
        elif angle == 180:
            matrix = rotate_180(matrix)
        elif angle == 270:
            matrix = rotate_270(matrix)
        else:  # 360
            matrix = rotate_360(matrix)

        # 결과 출력
        print_matrix(matrix)


if __name__ == "__main__":
    solve()
