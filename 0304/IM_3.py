import sys
sys.stdin = open("txt/IM.txt", "r")

'''
6 10 9
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_count = 1

    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 1   # 각 지점별 count = 1

            while True:     # 탐색 시작
                min_v = 99
                min_i, min_j = -1, -1
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni = x + di
                    nj = y + dj
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < matrix[x][y] and matrix[ni][nj] < min_v:
                        min_i, min_j = ni, nj
                        min_v = matrix[ni][nj]

                if min_i == -1:
                    break
                
                # 최소값 탐색 성공시
                count += 1  # 길이 +1
                x, y = min_i, min_j     # 현 위치 갱신

            max_count = max(max_count, count)



    print(f'#{tc} {max_count}')
