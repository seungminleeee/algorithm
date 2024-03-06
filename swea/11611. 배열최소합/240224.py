import sys
sys.stdin = open('input.txt')

def dfs(n, sumv):
    global minv
    if n == N:
        if minv > sumv:
            minv = sumv
        return
    if minv <= sumv:
        return
    for i in range(N):
        if visited[i] != 1:
            visited[i] = 1
            dfs(n+1, arr[n][i] + sumv)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    minv = 99999999999
    dfs(0,0)
    print(f'#{tc} {minv}')