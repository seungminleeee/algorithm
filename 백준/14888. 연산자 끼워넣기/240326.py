import sys; sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
ope = list(map(int, input().split()))

mn = 1000000000
mx = -1000000000

def f(n, sm):
    global mn, mx, ope
    if n == N:
        mn = min(sm, mn)
        mx = max(sm, mx)
        return

    if sm < -1000000000 or sm > 1000000000:
        return

    for i in range(4):
        if ope[i] >= 1:
            ope[i] -= 1
            if i == 0:      # +
                f(n+1, sm + arr[n])
            elif i == 1:    # -
                f(n+1, sm - arr[n])
            elif i == 2:    # *
                f(n+1, sm * arr[n])
            elif i == 3:    # /
                if arr[n] < 0:  # 음수로 나눌 때
                    f(n+1, int(-(sm / (-arr[n]))))
                elif arr[n] > 0:    # 양수로 나눌 때
                    f(n+1, int(sm / arr[n]))
                else:   # 0 으로 나눌 때
                    continue
            ope[i] += 1

f(1, arr[0])
print(mx)
print(mn)