import sys; sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split())) + [0]

cnt = 0
max_diff = 0
for i in range(N):
    if arr[i] < arr[i+1]: # 다음 수가 크면 숫자 1 올라감
        cnt += 1
    else:   # 다음 수가 작으면 숫자 초기화, 찾은 최대 차이값과 현재 오르막 차이 비교
        max_diff = max(max_diff, arr[i] - arr[i - cnt])
        cnt = 0

print(max_diff)