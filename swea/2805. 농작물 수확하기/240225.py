import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    M = N // 2
    sum_v = 0

    s = e = M
    for r in range(N):
        for c in range(s, e+1):
            sum_v += arr[r][c]
        if r < M:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1


    print(f'#{tc} {sum_v}')