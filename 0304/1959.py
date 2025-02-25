import sys
sys.stdin = open("txt/1959.txt", "r")

def max_multi(N, M):

    max_num = 0
    if N <= M:
        for j in range(M-N+1):# 0 1 2
            mul = 0
            for i in range(N):
                mul += A[i] * B[i+j]
            max_num = max(mul, max_num)
        return max_num
    else:
        for j in range(N-M+1):# 0 1 2
            mul = 0
            for i in range(M):
                mul += A[i+j] * B[i]
            max_num = max(mul, max_num)
        return max_num




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = max_multi(N, M)



    print(f'#{test_case} {ans}')