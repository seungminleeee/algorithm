import sys; sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
Max = 60

def dfs(r,c):
    global visited
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if arr[nr][nc] and not visited[nr][nc] and 0<=nr<=N and 0<=nc<=M:
            dfs(nr, nc)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*Max for _ in range(Max)]
    visited = [[0]*Max for _ in range(Max)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y+1][x+1] = 1

    cnt = 0
    for r in range(1, N+1):
        for c in range(1, M+1):
            if arr[r][c] and not visited[r][c]:
                dfs(r,c)
                cnt += 1

    print(cnt)


####################################
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def dfs(r, c):
#     global visited
#     visited[r][c] = 1
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
#             dfs(nr, nc)
#
# T = int(input())
# for tc in range(T):
#     M, N, K = map(int, input().split())
#     arr = [[0]*M for _ in range(N)]
#     visited = [[0]*M for _ in range(N)]
#
#     for _ in range(K):
#         x, y = map(int, input().split())
#         arr[y][x] = 1
#
#     cnt = 0
#     for r in range(N):
#         for c in range(M):
#             if arr[r][c] and not visited[r][c]:
#                 dfs(r, c)
#                 cnt += 1
#
#     print(cnt)
