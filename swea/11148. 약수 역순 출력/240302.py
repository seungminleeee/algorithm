import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = []
    for i in range(N, 0, -1):
        if N % i == 0:
            lst.append(i)

    print(f"#{tc}",' '.join(map(str, lst)))