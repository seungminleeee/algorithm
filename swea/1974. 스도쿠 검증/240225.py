import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    # 가로줄 보기
    for r in range(9):
        lst = []
        for c in range(9):
            if arr[r][c] not in lst:
                lst.append(arr[r][c])
            else:
                ans = 0
                break


    # 세로줄 보기
    for c in range(9):
        lst = []
        for r in range(9):
            if arr[r][c] not in lst:
                lst.append(arr[r][c])
            else:
                ans = 0
                break


    # 3*3칸 보기
    lst = []
    s = 0
    for r in range(s, s+3):
        e = 0
        for c in range(e, e+3):
            if arr[r][c] not in lst:
                lst.append(arr[r][c])
            else:
                ans = 0
                break
            e += 3
        s += 3

    print(f'#{tc} {ans}')