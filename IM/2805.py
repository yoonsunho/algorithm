import sys
sys.stdin = open("txt/2805.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 농장의 크기(1 ≤ N ≤ 49)

    farm_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        farm_arr[i] = list(map(int, input()))

    benefit = 0
    for i in range(N//2+1):
        for j in range(N//2-i,N//2+i+1):
            benefit += farm_arr[i][j]

    for i in range(N//2):   # 0 1 2
        for j in range(N//2-i, N//2+i+1):
            benefit += farm_arr[-i-1][j]



    print(f'#{test_case} {benefit}')