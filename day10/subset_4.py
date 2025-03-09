# 나머지 원소의 합을 알떄
def f(i, N, s, t, rs):     # i: 인덱스, N: 배열 크기,s: i-1 까지 결정한 원소의 합,t: 찾는 합
    global cnt
    cnt += 1
    if s == t:  # 찾았니?
        print(bit, s)
        return
    elif s > t:       # 더 크니?
        return
    elif i == N:        # 끝났니?
        return
    elif s + rs < t:       # 남은 원소를 다 더해도 찾을 수 없으면
        return      # 2047 -> 21
    else:
        bit[i] = 1      # bit[i]를 1 로 결정d
        f(i+1, N, s + A[i],t, rs - A[i])        # bit[i+1] 결정하러 이동
        bit[i] = 0
        f(i+1, N, s,t, rs-A[i])

A = [1, 2, 3,4,5,6,7,8,9,10]
bit = [0] * len(A)
cnt = 0
f(0, len(A), 0, 55, sum(A))
print(cnt)