import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    t = lst[0]
    arr = lst[1:]
    N = 20
    n_arr = []
    cnt = 0
    for i in range(N):
        if len(n_arr) != 0 and max(n_arr) < arr[i]:
            n_arr.append(arr[i])
        else:
            cnt += len(n_arr)
            n_arr.insert(0, arr[i])

    print(t, cnt)
