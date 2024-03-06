import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    lst = [0]
    for i in range(N):
        if arr[i] not in lst:
            lst.append(arr[i])

    M = len(lst)
    for k in range(M):
        for l in range(k+1, M):
            if lst[k] > lst[l]:
                lst[k], lst[l] = lst[l], lst[k]

    for j in range(M):
        if j == K:
            ans = lst[j]
            break

    print(f'#{tc} {ans}')