import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sr, sc, N = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]

    for r in range(sr, sr + N):
        for c in range(sc, sc + N):
            if r == sr or r == sr+N-1:
                arr[r][c] = 1
            elif c == sc or c == sc+N-1:
                arr[r][c] = 1

    print(f'#{tc}')
    for line in arr:
        print(*line)