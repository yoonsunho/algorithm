import sys
sys.stdin = open("txt/16268.txt", "r")

# 7m

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    pang = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = pang[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += pang[ni][nj]
            max_v = max(max_v, cnt)

    print(f'#{tc} {max_v}')