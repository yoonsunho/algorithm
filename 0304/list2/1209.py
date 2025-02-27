import sys
sys.stdin = open("txt/1209.txt", "r")

# 10m

for _ in range(1, 11):

    T = int(input())

    matrix = [list(map(int,input().split())) for _ in range(100)]

    max_v = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            col_sum += matrix[i][j]
            row_sum += matrix[j][i]
        max_v = max(max_v, row_sum)
        max_v = max(max_v, col_sum)

    sl_sum = 0
    re_sum = 0
    for i in range(100):
        sl_sum += matrix[i][i]
        re_sum += matrix[i][99-i]
    max_s = max(sl_sum,re_sum)
    max_v = max(max_v, max_s)


    print(f'#{T} {max_v}')