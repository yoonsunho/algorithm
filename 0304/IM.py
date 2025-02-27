import sys
sys.stdin = open("txt/IM.txt","r")

def find_min(i, j, cnt):
    min_v = 99

    for di, dj in [[0, 1],[1,0],[0,-1],[-1,0]]:

        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < matrix[i][j]:
            if matrix[ni][nj] < min_v:
                min_i, min_j = ni, nj
                min_v = matrix[ni][nj]
        # def(min_i,min_j)
    # return find_min(min_i, min_j, cnt+1)
    return find_min(min_i,min_j,cnt+1)



'''
6 10 9
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    count = []       # 최대 이동거리를 담을 변수
    for i in range(N):
        for j in range(N):
            cnt = 1
            count.append(find_min(i,j,cnt))
    print(count)


    print(f'#{tc} ')
