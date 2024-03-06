import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())

    print(f'#{tc}')
    if M == 1:
        for i in range(1,N+1):
            print('*' * i)
    elif M == 2:
        for i in range(N, 0, -1):
            print('*' * i)
    else:
        for i in range(1,N+1):
            print(' '*(N-i), end = '')
            cnt = (i-1) + i
            print('*'*cnt)