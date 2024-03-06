import sys; sys.stdin = open('input.txt')

H, W = map(int,input().split())
cloud = [list(map(str, input())) for _ in range(H)]

arr = [[-1]*W for _ in range(H)]    # 전체 -1로 배열 깔아둠
for r in range(H):
    for j in range(W):
        if cloud[r][j] == '.':  # 구름이 없던 자리면
            for k in range(W, 0, -1):
                if 0<= j-k < W and cloud[r][j-k] == 'c':    # 이전에 구름이 있었는지 확인
                    arr[r][j] = k   # 이전 구름 있으면 차이만큼 입력
        else:
            arr[r][j] = 0   # 구름이 있던 자리는 0 저장

for line in arr:
    print(*line)