def f(i, N, s, t):       # i인덱스, N 배열 크기. i-1까지 결정한 원소의 합
    global cnt
    cnt += 1
    if s > t:   # 찾는 합보다 커지면 중지
        return
    if i == N:
        if s == t:  # 찾는 값이면
            print(bit, s)
        elif s > t:     # 찾는 합보다 커지면 중지
            return
        elif i == N:
            return
        elif s + rs < t:    # 남은 원소를 다 더해도 찾을 수 없으면
            return 
    else:
        bit[i] = 1      # bit[i]를 1로 결정
        f(i+1, N, s+A[i],t,rs-A[i])
        bit[i] = 0
        f(i+1,N,s,t,rs-A[i])

A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * len(A)
cnt = 0
f(0,len(A),0,55)
print(cnt)