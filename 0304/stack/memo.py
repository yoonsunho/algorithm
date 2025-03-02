n = int(input())
memo = [0] * (n+1)

memo[0] = 0
memo[1] = 1

def fibo1(n):
    global memo
    if n >= 2:
        memo[n] = fibo1(n-1)+fibo1(n-2)

    return memo[n]

print(fibo1(n))