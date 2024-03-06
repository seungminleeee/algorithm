import sys
sys.stdin = open('input.txt')

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[r][c] > arr[nr][nc]:
                        cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')