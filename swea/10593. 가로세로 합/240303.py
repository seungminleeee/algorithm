import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    max_v = 0
    for r in range(N):
        for c in range(N):
            sum_v = arr[r][c]
            for i in range(4):
                for j in range(1, N):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_v += arr[nr][nc]
            max_v = max(sum_v, max_v)

    print(f'#{tc} {max_v}')