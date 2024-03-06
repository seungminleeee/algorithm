N = int(input())

cnt = 0
while N > 0:
    if N % 5 == 0:  # 5로 나누어 떨어지면
        cnt += N // 5   # 카운트에 5로 나눈 몫만큼 더해줌 (5를 뺀 횟수와 같으니까)
        break
    N -= 3
    cnt += 1    # 3 뺄때마다 카운트 증가

if N < 0:   # n이 음수이면 카운트 -1
    cnt = -1

print(cnt)
