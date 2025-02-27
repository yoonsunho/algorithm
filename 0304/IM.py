import sys
sys.stdin = open("txt/IM.txt","r")

'''
6 10 9
'''

def move(i,j)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_v = 1       # 최대 이동거리를 담을 변수
    for i in range(N):
        for j in range(N):
            min_v = 99
            for di, dj in [[0, 1],[1,0],[0,-1],[-1,0]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj <N and matrix[ni][nj] < matrix[i][j]:
                    x = matrix[ni][nj]
                    min_v = min(min_v, x)

    print(f'#{tc} ')
