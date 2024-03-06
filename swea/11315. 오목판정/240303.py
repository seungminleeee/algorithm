import sys;sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]

    ret = 'NO'
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                cnt = 1
                for i in range(4):
                    for j in range(1, 5):
                        nr = r + dr[i]*j
                        nc = c + dc[i]*j
                        if not(0<=nr<N and 0<=nc<N):
                            break
                        if arr[nr][nc] != 'o':
                            break
                    else:
                        ret = 'YES'

    print(f'#{tc} {ret}')