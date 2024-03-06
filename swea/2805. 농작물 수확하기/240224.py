import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    M = N // 2
    sum_v = 0
    for r in range(0, N):
        if r <= M:
            for c in range(M-r, M+r+1):
                sum_v += arr[r][c]
        else:
            for c in range(r-M, N-r+M):
                sum_v += arr[r][c]

    print(f'#{tc} {sum_v}')