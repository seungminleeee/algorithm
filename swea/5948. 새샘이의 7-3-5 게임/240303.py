import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    lst = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                val = arr[i]+arr[j]+arr[k]
                if val not in lst:
                    lst.append(val)

    lst. sort(reverse=True)
    ans = lst[4]
    print(f'#{tc} {ans}')