def f(i, N):     # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)        # i+1 자리 결정
            p[i], p[j] = p[j], p[i]     # 원상복구


p = [0,1,2]
N = 5
f(0, N)