import sys; sys.stdin = open('input.txt')

import sys; sys.setrecursionlimit(10**6)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 적록색약일 경우
def fyes(r,c):
    vyes[r][c] = 1
    color = arr[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc] == color and vyes[nr][nc]==0:
            fyes(nr,nc)

# 적록색약 아닐 경우
def fno(r,c):
    vno[r][c] = 1
    color = arr_o[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and arr_o[nr][nc] == color and vno[nr][nc]==0:
            fno(nr,nc)

N = int(input())
arr_o = [list(input()) for _ in range(N)]
arr = [[0]*N for _ in range(N)] # 적록색약일 경우 G-> R로 바꿀 배열

vyes = [[0]*N for _ in range(N)] # 적록색약일 경우
vno = [[0]*N for _ in range(N)] # 적록색약 아닐 경우

for r in range(N):
    for c in range(N):
        if arr_o[r][c] == 'G':
            arr[r][c] = 'R'
        else:
            arr[r][c] = arr_o[r][c]

# 적록색약일 경우
yescnt = 0
for r in range(N):
    for c in range(N):
        if vyes[r][c] == 0:
            fyes(r,c)
            yescnt += 1

# 적록색약 아닐 경우
nocnt = 0
for r in range(N):
    for c in range(N):
        if vno[r][c] == 0:
            fno(r,c)
            nocnt += 1


print(nocnt, yescnt)