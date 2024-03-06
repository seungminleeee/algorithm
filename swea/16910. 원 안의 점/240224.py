import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if i == 0 and j == 0:
                cnt +=1
            elif i == 0 and j != 0 and j ** 2 <= N**2:
                cnt += 2
            elif j == 0 and i !=0 and i ** 2 <= N ** 2:
                cnt += 2
            elif i != 0 and j != 0 and i**2 + j **2 <= N**2:
                cnt += 4

    print(f'#{tc} {cnt}')