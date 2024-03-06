import sys; sys.stdin = open('input.txt')

L = int(input())
N = int(input())

people = []
cake = [0] * (L+2)
for a in range(1, N+1):
    P, K = map(int, input().split())
    people.append((a,P,K))  # 방청객 번호, P~K번 조각 저장

    for b in range(P, K+1): # 조각에 방청객 번호 저장
        if cake[b] == 0:
            cake[b] = a

# 기대
max_hope = 0    # 최대 조각 수 저장할 부분
hope_person = 0     # 방청객 번호 저장할 부분
for i in range(N):
    hope_pieces = people[i][2] - people[i][1] + 1
    if hope_pieces > max_hope:
        max_hope = hope_pieces    # 기대하는 최대 조각 수 저장
        hope_person = i + 1     # 기대 조각수가 최대일때 방청객 번호 저장
print(hope_person)

# 실제
cnt_lst = [0]*(N+1)     # 방청객이 받는 조각 수 입력할 리스트
for c in cake:
    cnt_lst[c] += 1     # 조각수 입력
max_real = max(cnt_lst[1:])     # 실제 최대 조각수
ans = cnt_lst.index(max_real)       # 실제 최대 조각수의 인덱스 = 방청객 번호

print(ans)
