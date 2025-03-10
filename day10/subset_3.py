# 찾는 부분집합 값 찾을 떄 까지

def f(i, N, s, t):     # i: 인덱스, N: 배열 크기,s: i-1 까지 결정한 원소의 합,t: 찾는 합
    global cnt
    cnt += 1
    if s == t:  # 찾는 값이면 => 또 더 줄일 수 있음
        print(bit, s)
        return
    elif s > t:       # 찾는 합 보다 커지면 중지 (횟수 확 줄일 수 있음)(백 트래킹의 장점)(but 최악의 경우 원래와 상황 동일)
        return
    elif i == N:
        return
    else:
        bit[i] = 1      # bit[i]를 1 로 결정d
        f(i+1, N, s + A[i],t)        # bit[i+1] 결정하러 이동
        bit[i] = 0
        f(i+1, N, s,t)

A = [1, 2, 3,4,5,6,7,8,9,10]
bit = [0] * len(A)
cnt = 0
f(0, len(A), 0, 2)
print(cnt)