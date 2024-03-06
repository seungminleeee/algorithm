import sys
sys.stdin = open('input.txt')

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, 1, -1, -1, 0, 1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    n = N//2
    arr[n][n] = arr[n+1][n+1] = 2
    arr[n][n+1] = arr[n+1][n] = 1

    for _ in range(M):
        sc, sr , color = map(int, input().split())
        arr[sr][sc] = color

        for i in range(8):
            lst = []
            for j in range(1, N):
                nr = sr + dr[i]*j
                nc = sc + dc[i]*j
                if 0<=nr<=N and 0<=nc<=N:
                    if arr[nr][nc] == 0:
                        break
                    elif arr[nr][nc] == color:
                        while lst:  # 저장해둔 돌 뒤집기
                            tr, tc = lst.pop()
                            arr[tr][tc] = color
                        break
                    else:   # 색다른 돌 있으면 저장 해두기
                        lst.append((nr,nc))
                else:
                    break

    black = 0
    white = 0
    for line in arr:
        black += line.count(1)
        white += line.count(2)

    print(f'#{t} {black} {white}')