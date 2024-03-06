import sys
sys.stdin = open('input.txt')

def increase(val):
    val_s = str(val)
    n = len(val_s)
    for a in range(n-1):
        if val_s[a] > val_s[a+1]:
            return False
    return True


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = -1
    for i in range(N-1):
        for j in range(i+1,N):
            num = arr[i]*arr[j]
            if increase(num) and ans < num:
                ans = num

    print(f'#{tc} {ans}')