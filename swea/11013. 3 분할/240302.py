import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ret = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            A = arr[:i]
            B = arr[i:j]
            C = arr[j:]
            diff = max(sum(A), sum(B), sum(C)) - min(sum(A), sum(B), sum(C))
            ret.append(diff)

    print(f'#{tc}',min(ret))