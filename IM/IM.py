import sys
sys.stdin = open("txt/11315.txt", "r")

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    hei = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            min_i, min_j = i, j
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                count = 0
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0<= nj < N:
                    min_i = ni
                    min_j = nj




    print(f'#{tc}')