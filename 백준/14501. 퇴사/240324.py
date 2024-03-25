import sys;sys.stdin = open('input.txt')

def dfs(n,sm):
    global ans
    # 1. 종료조건 : 가능한 n을 종료에 관련된 것으로 정의
    if n >= N:
        ans = max(ans, sm)
        return

    # 2. 하부 호출 : 화살표 개수만큼
    if n + T[n] <= N:
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0,0)
print(ans)