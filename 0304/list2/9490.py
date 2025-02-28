import sys
sys.stdin  = open("txt/9490.txt", "r")

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    poong = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            pung_sum = poong[i][j]
            for x in range(4):
                for k in range(1, poong[i][j]+1):
                    ni = i + di[x] * k
                    nj = j + dj[x] * k
                    if 0 <= ni < N and 0 <= nj < M:
                        pung_sum += poong[ni][nj]
            max_v = max(max_v, pung_sum)


    print(f'#{tc} {max_v}')