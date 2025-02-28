import sys
sys.stdin = open("txt/1210.txt", "r")

# 1h 20m
# while true 첨으로 구현해서 성공 ㅜㅜ

for _ in range(1, 11):
    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if ladder[99][j] == 2:
            st_i, st_j = 99, j      # 출발 지점 지정

    # print(st_j)
    next_i, next_j = -1, -1
    ladder[st_i][st_j] = 0

    while True:
        # ladder[st_i][st_j] == 0
        for di, dj in [[0, 1], [0, -1], [-1, 0]]:
            ni = st_i + di
            nj = st_j + dj
            if 0 <= ni < 100 and 0 <= nj < 100:
                if ladder[ni][nj] == 1:
                    ladder[ni][nj] = 0
                    next_i, next_j = ni, nj
                    break


        if next_i == 0:
            # print(next_j)
            break

        st_i, st_j = next_i, next_j




    print(f'#{tc} {next_j}')