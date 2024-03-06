import sys; sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)]
arr.sort()  # 오름차순 정렬하기
pick = [0]*7

# 합이 100이 되는 조합 찾기
def comb(k, start,total):
    if k == 7:  # 7번째까지 골랐으면 함수 종료
        if total == 100:    # 합이 100이 됐을때 순서대로 출력
            for i in range(7):
                print(pick[i])
            exit()      # 처음에 return으로 썼는데 틀렸다고 해서 바꿈
        return
    for i in range(start, 9):
        pick[k] = arr[i]
        comb(k+1, i+1, total+arr[i])

comb(0,0,0)
