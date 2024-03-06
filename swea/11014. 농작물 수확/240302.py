import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ret = 999999999

    for _ in range(N):
        for r in range(N):
            for c in range(N):
                A = []
                B = []
                C = []
                for i in range(1, N):
                    if r + i < N and c + i < N:
                        A.append(arr[r][c + i])
                        if r - i >= 0 and c - i >= 0:
                            B.append(arr[r - i][c - i])
                        if r + i < N and c - i >= 0:
                            C.append(arr[r + i][c - i])
        # if len(A) != 0 and len(B) !=0 and len(C) !=0:
        X = max(sum(A), sum(B), sum(C))
        Y = min(sum(A), sum(B), sum(C))
        ret = min(X - Y, ret)

    print(f"#{tc} {ret}")
