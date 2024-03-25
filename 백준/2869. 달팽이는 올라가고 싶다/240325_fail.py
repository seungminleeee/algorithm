#런타임 에러

A, B, V = map(int, input().split())

cnt = 0
ans = 0
while ans <= V:
    cnt += 1
    ans += A
    if ans >= V:
        break
    ans -= B


print(cnt)