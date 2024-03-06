import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        max_v = 0
        for i in range(M-N+1):
            sum_v = 0
            for j in range(N):
                sum_v += A[j]*B[j]
            if max_v < sum_v:
                max_v = sum_v

            A = [0] + A
            N = len(A)

    elif N > M:
        max_v = 0
        for i in range(-M+N+1):
            sum_v = 0
            for j in range(M):
                sum_v += A[j]*B[j]
            if max_v < sum_v:
                max_v = sum_v

            B = [0] + B
            M = len(B)

    else:
        max_v = 0
        for i in range(N):
            max_v += A[i]*B[i]


    print(f'#{tc}', max_v)