import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    # 가로 확인
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += arr[r][c]
            else:
                if cnt > 1:
                    lst.append(cnt)
                cnt = 0
        if cnt > 1:
            lst.append(cnt)

    # 세로 확인
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] !=0:
                cnt += arr[r][c]
            else:
                if cnt > 1:
                    lst.append(cnt)
                cnt = 0
        if cnt > 1:
            lst.append(cnt)

    # print(lst)
    ret = 0
    for num in lst:
        if num == K:
            ret += 1

    print(f'#{tc} {ret}')