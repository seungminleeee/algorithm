import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, num = map(str, input().split())
    N = int(N)

    ans = ''
    for n in num:
        a = format(int(n, 16), '04b')
        ans += a

    print(f'#{tc}', ans)