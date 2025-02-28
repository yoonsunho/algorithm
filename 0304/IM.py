import sys
sys.stdin = open("txt/IM.txt","r")

# 꼭 다시 풀어보기.....

'''
6 10 9
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_count = 1      # 최대 이동거리를 담을 변수

    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 1

            while True:
                min_v = 99
                min_i, min_j = -1, -1
                for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
                    ni = x + di
                    nj = y + dj
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < matrix[x][y] and matrix[ni][nj] < min_v:
                        # if matrix[ni][nj] < min_v:
                        min_i, min_j = ni, nj
                        min_v = matrix[ni][nj]

                if min_i == -1:
                    break

                x, y = min_i, min_j
                count += 1

            max_count = max(max_count, count)

    print(f'#{tc} {max_count}')
