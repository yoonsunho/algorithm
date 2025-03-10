# 그때 그떄 합 갱신하는 방식

def f(i, N, s):     # i: 인덱스, N: 배열 크기, i-1 까지 결정한 원소의 합
    global cnt
    cnt += 1
    if i == N:
        print(bit, s)
        s = 0
    else:
        bit[i] = 1      # bit[i]를 1 로 결정
        f(i+1, N, s + A[i])        # bit[i+1] 결정하러 이동
        bit[i] = 0
        f(i+1, N, s)

A = [1, 2, 3]
bit = [0] * len(A)
cnt = 0
f(0, len(A), 0)
print(cnt)  # 15(부분집합의 수 만큼)
