import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for c in range(N):
        for r in range(N):
            if arr[r][c] == 1:
                for i in range(r+1, N):
                    if arr[i][c] == 2:
                        cnt += 1
                        arr[i][c] = 0
                        break
                    if arr[i][c] == 1:
                        break

    print(f'#{tc}', cnt)