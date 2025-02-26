import sys
sys.stdin = open("txt/4836.txt", "r")

# 10m
# 다시 안풀어도 될듯

T = int(input())
for tc in range(1, T+1):

    N = int(input())        # 색칠할 영역의 개수

    color_matrix = [[0]*10 for _ in range(10)]
    cnt = 0

    for _ in range(N):

        st_i, st_j, en_i, en_j, color = map(int, input().split())

        for i in range(st_i, en_i+1):
            for j in range(st_j, en_j+1):
                color_matrix[i][j] += color

    #
    # for i in range(10):
    #     print(color_matrix[i])

    for i in range(10):
        for j in range(10):
            if color_matrix[i][j] == 3:
                cnt += 1


    print(f'#{tc} {cnt}')