# 약수 쌍 찾는 방법 생각함
N = int(input())
nums = {i for i in range(1, N+1)}
cnt = 1

for num in nums:
    lst = {1}   # 약수 넣을 리스트
    for j in range(2, num+1):   # 약수 1은 항상 포함이니까 2부터
        if num % j == 0 and j not in lst:   # 약수이고 리스트에 없으면
            cnt += 1    # 카운트 1 증가
            lst.add(j)
            if num//j not in lst:   # 약수 쌍(?) 없으면 포함하기
                lst.add(num//j)
        elif j >= N:    # 찾아야하는 수보다 커지면
            break

print(cnt)