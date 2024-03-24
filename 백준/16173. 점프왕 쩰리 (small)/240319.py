import sys; sys.stdin = open('input.txt')

dr = [0, 1]
dc = [1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]

ans = 'Hing'

def f(r, c):
    global ans
    if r >= N-1 and c >= N-1:
        if arr[r][c] == -1:
            ans = 'HaruHaru'
        return

    for i in range(2):
        nr = r + dr[i] * arr[r][c]
        nc = c + dc[i] * arr[r][c]
        if 0<=nr <N and 0<=nc <N and v[nr][nc] == 0:
            v[nr][nc] = 1
            f(nr, nc)

f(0, 0)
print(ans)


