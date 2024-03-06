N = int(input())
for number in range(1, N+1):
    num = str(number)

    cnt = 0
    for val in num:
        if val in '369':
            cnt += 1

    if cnt >= 1:
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')