import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    t = lst[0]
    arr = lst[1:]
    N = 20
    cnt = 0

    for i in range(1, N):
        for j in range(i):  # i번째 앞까지 순회하면서 i번째보다 크면 자리 바꾸기
            if arr[j] > arr[i]:
                cnt += 1    # 자리바꾸면 cnt 1 증가
                arr[j], arr[i] = arr[i], arr[j]
    print(t, cnt)
