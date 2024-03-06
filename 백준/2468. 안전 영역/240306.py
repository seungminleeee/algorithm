import sys; sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

from collections import deque
def bfs(sr, sc, h):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        qr, qc = q.popleft()
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] >h and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1

def func(h):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0 and arr[r][c] > h:
                bfs(r, c, h)
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


ans = 0
for h in range(100):
    visited = [[0]*N for _ in range(N)]
    ans = max(ans, func(h))

print(ans)

