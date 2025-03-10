def f(i, N):     # i: 인덱스, N: 배열 크기
    if i == N:
        print(bit)
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
        print(s)
    else:
        bit[i] = 1      # bit[i]를 1 로 결정
        f(i+1, N)        # bit[i+1] 결정하러 이동
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3]
bit = [0] * len(A)
f(0, len(A))
'''
[1, 1, 1]
6
[1, 1, 0]
3
[1, 0, 1]
4
[1, 0, 0]
1
[0, 1, 1]
5
[0, 1, 0]
2
[0, 0, 1]
3
[0, 0, 0]
0
'''
