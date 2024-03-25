import sys; sys.stdin = open('input.txt')

A = int(input())
B = input()

for b in B[::-1]:
    ans = A*int(b)
    print(ans)

print(A*int(B))