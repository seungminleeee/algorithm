import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]

    max_v = 0
    for r in range(N):
        for c in range(N):
            sum_v = 0
            for i in range(M):
                for j in range(M):
                    if 0 <= r+i < N and 0 <= c+j < N:
                        sum_v += arr[r+i][c+j]
            if sum_v > max_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')