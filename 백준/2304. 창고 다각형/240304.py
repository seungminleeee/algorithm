import sys; sys.stdin = open('input.txt')

N = int(input())

L_lst = []
H_lst = []
for _ in range(N):
    L, H = map(int, input().split())
    L_lst.append(L)
    H_lst.append(H)

M = max(L_lst)
arr = [0]*(M+1)

for i in range(M+1):
    try:
        arr[L_lst[i]] = H_lst[i]
    except:
        pass

max_H = max(H_lst)
max_idx = arr.index(max_H)

for i in range(1, max_idx):
    if arr[i] > arr[i+1]:
        arr[i+1] = arr[i]

for j in range(M, max_idx, -1):
    if arr[j] > arr[j-1]:
        arr[j-1] = arr[j]

print(sum(arr))