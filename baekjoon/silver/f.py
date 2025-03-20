def factorial(n):

    if n >= 2 and memo[n] == 0:
        print(n)
        memo[n] = n * factorial(n-1)
        print(memo[n])
    return memo[n]

N = 3
M = 3
memo = [0]*(N+1)  # N 일 때의 최대 다리 개수

memo[0] = 1
memo[1] = 1
print(factorial(3))