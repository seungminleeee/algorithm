import sys; sys.stdin = open('input.txt')

import sys; sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def f(r,c):
    global cnt
    visited[r][c] = 1
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<M and 0<=nc<N and arr[nr][nc] ==0 and visited[nr][nc] == 0:
            f(nr, nc)
    return cnt


M, N, K = map(int, input().split())
arr=[[0]*N for _ in range(M)]
visited=[[0]*N for _ in range(M)]
for _ in range(K):
    x, y, a, b = map(int, input().split())
    for i in range(y, b):
        for j in range(x, a):
            arr[i][j] = 1

cnt = 0
area = []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and visited[r][c] == 0:
            f(r,c)
            area.append(cnt)
            cnt = 0

area.sort()
print(len(area))
print(' '.join(map(str,area)))