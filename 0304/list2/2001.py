import sys
sys.stdin = open("txt/2001.txt","r")
# 5m 30s

T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())

    pari = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += pari[i+k][j+l]
            max_v = max(cnt, max_v)



    print(f'#{tc} {max_v}')