import sys
sys.stdin = open("txt/18575.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        matrix[i] = list(map(int, input().split()))

    max_sum = 0
    min_sum = 100000
    for i in range(N):
        for j in range(N):
            sum = matrix[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1, N):
                    ni = i + k * di
                    nj = j + k * dj

                    if 0 <= ni < N and 0 <= nj < N:
                        sum += matrix[ni][nj]
            max_sum = max(max_sum,sum)
            min_sum = min(min_sum,sum)

    ans = max_sum-min_sum

    print(f'#{test_case} {ans}')