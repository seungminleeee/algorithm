import sys; sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split())) + [0]

ans = 0
max_ans = 0
for i in range(N):
    if arr[i] < arr[i+1]:
        ans += arr[i+1] - arr[i]
    else:
        max_ans = max(ans, max_ans)
        ans = 0

print(max_ans)