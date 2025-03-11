def f(i, N, s):
    global min_v
    global cnt
    cnt += 1
    if i == N:
        # s = 0
        # for j in range(N):  # j 행에서 고른 열 p[j]
        #     s += arr[j][p[j]]
            # print(s)
        min_v = min(min_v, s)
    elif min_v < s:     # 중간 합계가 최솟값 보다 크면 그만해 => cnt 연산횟수 줄일 수 있음
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리 교환
            f(i+1, N, s + arr[i][p[i]])   # i+1 자리 결정
            p[i], p[j]= p[j], p[i]      # 원상 복구

N = int(input())    # 배열의 크기 N x N
arr = [list(map(int,input().split())) for _ in range(N)]

p = [i for i in range(N)]   # P[i] : i 행에서 고른 열 번호
# print(p)
min_v = 10000
cnt = 0     # 횟수
f(0, N, 0)
print(min_v, cnt)