import sys;sys.stdin = open('input.txt')
from collections import deque

def dfs(n):
    global visited
    visited[n] = 1
    print(n, end =' ')
    for a in range(1,N+1):
        if visited[a] == 0 and graph[n][a] == 1:
            dfs(a)

def bfs(n):
    q = deque()
    global visited
    visited[n] = 1
    q.append(n)

    while q:
        now = q.popleft()
        print(now, end =' ')

        for to in range(1, N+1):
            if visited[to] == 0 and graph[now][to] == 1:
                visited[to] = 1
                q.append(to)


N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V)
