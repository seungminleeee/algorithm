import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    maxv = 0
    for r in range(N):
        for c in range(M):
            sumv = arr[r][c]

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    sumv += arr[nr][nc]

                if sumv > maxv:
                    maxv = sumv

    print(f'#{tc} {maxv}')