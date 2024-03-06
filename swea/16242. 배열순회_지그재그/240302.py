import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sr, sc, W, H = map(int,input().split())
    arr = [[0] * 10 for _ in range(10)]

    num = 0
    cnt = 0
    for r in range(sr, sr+H):
        cnt += 1
        if cnt % 2 == 1:
            for c in range(sc, sc+W):
                num += 1
                arr[r][c] = num
        else:
            for c in range(sc+W-1, sc-1, -1):
                num += 1
                arr[r][c] = num

    print(f'#{tc}')
    for line in arr:
        print(*line)