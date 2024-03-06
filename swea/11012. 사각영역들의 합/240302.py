import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    for _ in range(M):
        sr, sc, length = map(int, input().split())

        for r in range(sr, sr+length):
            for c in range(sc, sc+length):
                if not(0<=r<N and 0<=c<N): break
                sum += arr[r][c]
                arr[r][c] = 0

    print(f'#{tc} {sum}')