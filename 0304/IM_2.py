import sys
sys.stdin = open("txt/IM.txt","r")

def move(i,j,count):

    print(i,j)


'''
6 10 9
'''

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    leng = []   # 각 지점 별 최대 거리 담을 배열
    for i in range(N):
        for j in range(N):
            cnt = 1
            min_v, min_i, min_j = 99, i, j
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < matrix[i][j] and matrix[ni][nj] < min_v:
                    min_i, min_j = ni, nj
                    min_v = matrix[ni][nj]
            move(min_i, min_j, cnt)
        else:
            leng.append(cnt)
            




    print(f'#{tc} ')
