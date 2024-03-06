import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    # sum = 0
    max_sum = 0
    for r in range(N):
        for c in range(N):
            sum_lst = []
            sum_lst.append(arr[r][c])
            for i in range(4):
                # sum_v = arr[r][c]
                for j in range(1, N):
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if 0 <= nr < N and 0 <= nc <N:
                        # sum_v += arr[nr][nc]
                        sum_lst.append(arr[nr][nc])
                sum_v = sum(sum_lst)
            max_sum = max(sum_v, max_sum)

    print(f'#{tc} {max_sum}')

