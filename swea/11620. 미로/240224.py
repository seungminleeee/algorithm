import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    visited[r][c] = 1
    global result

    if arr[r][c] == 3:
        result = 1
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0<= nc < N and arr[nr][nc] != 1 and visited[nr][nc] != 1:
            dfs(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    result = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                sr, sc = r, c

    dfs(sr, sc)
    print(f'#{tc} {result}')
