import sys
sys.stdin = open("txt/12712.txt", "r")

# 델타 탐색 부호 잘 보기

T = int(input())
for tc in range(1,T+1):

    N, M = map(int, input().split())

    pari = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            cnt = pari[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1,M):
                    ni = i + k * di
                    nj = j + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += pari[ni][nj]
            max_v = max(max_v, cnt)
    # print(max_v)

    for i in range(N):
        for j in range(N):
            c = pari[i][j]
            for di, dj in [[-1, 1], [1, 1],[1,-1],[-1,-1]]:
                for k in range(1,M):
                    ni = i + k * di
                    nj = j + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        c += pari[ni][nj]

            max_v = max(max_v, c)

    # print(max_v)




    print(f'#{tc} {max_v}')
