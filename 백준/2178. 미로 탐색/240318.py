import sys; sys.stdin = open('input.txt')
from collections import deque

def bfs(s, e):
    global visited, cnt
    Q = deque()
    visited[s][e] = 1
    Q.append((s,e, cnt))

    while Q:
        cs, ce, ccnt = Q.popleft()
        if cs == N-1 and ce == M-1:
            return ccnt

        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            ns = cs + dr
            nc = ce + dc
            if 0<=ns<N and 0<=nc<M and visited[ns][nc] == 0 and arr[ns][nc] == 1:
                visited[ns][nc] = 1
                Q.append((ns, nc, ccnt+1))

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]

cnt = 1


ans = bfs(0,0)
print(ans)