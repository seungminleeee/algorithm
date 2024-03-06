# 미완성

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    arr[N//2-1][N//2-1], arr[N//2][N//2] = 2, 2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1

    white = 0
    black = 0
    for _ in range(M):
        r, c, stone = map(int, input().split())
