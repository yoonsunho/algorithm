# 다리 끼리 겹칠 수 없음
# McN을 구하는 문제임(조합)
# 메모이제이셔을 사용한 팩토리얼?

def factorial(n):

    if n >= 2 and memo[n] == 0:
        memo[n] = n * factorial(n-1)

    return memo[n]

T = int(input())
for _ in range(T):

    N, M  = map(int, input().split())   #  (0 < N ≤ M < 30)

    # ans = 0
    memo = [0]*(M+1)  # N 일 때의 최대 다리 개수

    memo[0] = 1
    memo[1] = 1
    # memo[2] = 2

    ans = int(factorial(M)/(factorial(N)*factorial(M-N)))
    # dp[1] =M


    print(f'{ans}')