import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [[0]*W for _ in range(H)]

    num = 0
    for c in range(W):
        for r in range(H):
            num += 1
            arr[r][c] = num

    print(f'#{tc}')

    for line in arr:
        print(*line)