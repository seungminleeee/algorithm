import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))

    time.sort()

    cnt = 0
    for t in time:
        cnt += 1
        if t//M * K < cnt:
            ans = 'Impossible'
            break
        ans = 'Possible'

    print(f'#{tc} {ans}')