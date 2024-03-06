import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    nums = []
    for i in range(N-1):
        for j in range(i+1,N):
            nums.append(arr[i] * arr[j])

    lst = []
    for num in nums:
        num_s = str(num)
        for k in range(len(num_s)-1):
            for l in range(k+1,len(num_s)):
                if num_s[k] > num_s[l]:
                    break
                else:
                    lst.append(num)
    if len(lst) == 0:
        ans = -1
    else:
        ans = max(lst)

    print(f'#{tc} {ans}')