import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    s = 999
    e = 0
    max_v = -1
    for i in range(N):
        if A[i+1] >= A[i] and i+1 <N:
            if i < s:
                s = i
            if i+1 > e:
                e = i+1
            max_v = 0