import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]

    money = 0
    cnt = 0
    # lst = []
    for i in range(N):
        if arr[i] <= arr[i+1]:
            cnt += 1
            money -= arr[i]
        else:
            money += arr[i]*cnt
            cnt = 0

    print(f'#{tc} {money}')