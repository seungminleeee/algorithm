import sys
sys.stdin = open('input.txt')

def fly(sr, sc):
    sum_v = 0
    for r in range(sr, sr + M):
        for c in range(sc, sc + M):
            sum_v += arr[r][c]
    return sum_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]

    max_v = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            cnt = fly(r, c)
            if cnt > max_v:
                max_v = cnt

    print(f'#{tc} {max_v}')