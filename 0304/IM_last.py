import sys
sys.stdin = open("txt/IM.txt", "r")

# 20m

'''
6 10 9
'''
T = int(input())
for tc in range(1,T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_count = 1
    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 1
            while True:
                min_v = 99
                st_i, st_j = -1, -1
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = x + di, y + dj
                    if 0 <= ni < N and 0 <= nj <N and matrix[ni][nj]< matrix[x][y]:
                        if matrix[ni][nj] < min_v:
                            min_v = matrix[ni][nj]
                            st_i, st_j = ni, nj
                if st_i == -1:
                    break

                count += 1
                x,y = st_i, st_j

            max_count = max(max_count,count)


    print(f'#{tc} {max_count}')