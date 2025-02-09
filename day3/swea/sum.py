import sys
sys.stdin = open("sum.txt", "r")



for _ in range(10):

    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        max_sum = max(max_sum, row_sum)
        max_sum = max(max_sum, col_sum)

    di_sum = 0
    re_di_sum = 0
    for i in range(100):
        di_sum += arr[i][i]
        re_di_sum += arr[i][99-i]
    max_sum = max(max_sum, di_sum)
    max_sum = max(max_sum, re_di_sum)

    print(f'#{T} {max_sum}')