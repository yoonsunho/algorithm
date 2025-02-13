def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

cnt = 0     # 호출 횟수 기록(많이 일어남)
print(fibo(10), cnt)    # 55 177