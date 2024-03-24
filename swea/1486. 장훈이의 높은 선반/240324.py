import sys; sys.stdin = open('input.txt')

def dfs(sm, cnt):
    global mn

    if sm >= B:
        mn = min(mn, sm)

    if cnt == N:
        return

    dfs(sm + arr[cnt], cnt+1)
    dfs(sm, cnt + 1)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # N:점원수, B:선반 높이
    arr = list(map(int, input().split()))

    mn = 0xfffff
    dfs(0, 0)
    print(f'#{tc} {mn - B}')