import sys; sys.stdin = open('input.txt')

rlst = ['8', '7', '6', '5', '4', '3', '2', '1']
clst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
dlst = {'R':(0,1), 'L':(0,-1), 'B':(1,0), 'T':(-1,0),
        'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}

arr = [[0] * 8 for _ in range(8)]
king, stone, N = input().split()
N = int(N)
kr, kc = rlst.index(king[1]), clst.index(king[0])
sr, sc = rlst.index(stone[1]), clst.index(stone[0])

for _ in range(N):
    dr, dc = dlst[input()]

    nr = kr + dr
    nc = kc + dc

    if 0 <= nr < 8 and 0 <= nc < 8:
        if (nr, nc) == (sr, sc):
            xr = sr + dr
            xc = sc + dc
            if 0 <= xr < 8 and 0 <= xc < 8:
                sr, sc = xr, xc
                kr, kc = nr, nc
        else:
            kr, kc = nr, nc

K = clst[kc] + rlst[kr]
S = clst[sc] + rlst[sr]

print(K)
print(S)

