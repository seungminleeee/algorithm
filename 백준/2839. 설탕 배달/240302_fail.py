N = int(input())

n = N
cnt = 0
for i in range(1, N):
    if n % 5 >= 3 and n % 3 != 0:   # 3의 배수는 아니고 5로 나눠서 나머지가 3이상인수
        if n % 5 ==0:
            cnt += n // 5   # 5로 나눠 떨어지면 몫만큼 카운트 증가
            break
        else:
            cnt += n // 5
            n = n % 5
            if n % 3 == 0:
                cnt += n//3 # 3으로 나눠 떨어지면 몫만큼 카운트 증가
                break
            else:
                cnt = -1    # 둘 다 안되면 카운트 -1
                break
    else:
        if n % 3 == 0:  # 3의 배수이면
            cnt += n//3     # 카운트 몫만큼 증가
            break
        else:       # 둘다 아니면 카운트 -1
            cnt = -1


print(cnt)
# 틀린 이유 : 11 같이 3 나누기 먼저 해야하는 수를 고려하지 못함