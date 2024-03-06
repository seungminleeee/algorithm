# not complete

import sys; sys.stdin = open('input.txt')

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

black = 0
white = 0
win_r = 0
win_c = 0

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            cnt_1 = 1
            for i in range(4):
                for j in range(1,N):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if not (0<=nr<N and 0<=nc<N): break
                    if arr[nr][nc] == 0: break
                    cnt_1 += 1
                    win_r = min(win_r, nr)
                    win_c = min(win_c, nc)
                else:
                    if cnt_1 == 5:
                        black += 1

        if arr[r][c] == 2:
            cnt_2 = 1
            for i in range(4):
                for j in range(1,N):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if not (0<=nr<N and 0<=nc<N): break
                    if arr[nr][nc] == 0: break
                    cnt_2 += 1
                    win_r = min(win_r, nr)
                    win_c = min(win_c, nc)
                else:
                    if cnt_2 == 5:
                        white += 1

print(black, white, win_r, win_c)