import sys
sys.stdin = open("txt/sdocu.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    ans =1

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if row_sum != 45 or col_sum != 45:
            ans = 0


    for i in range(3):
        for j in range(3):
            box_sum = 0
            for k in range(3):
                for l in range(3):
                    box_sum += arr[3*i+k][3*i+l]
            if box_sum != 45:
                ans = 0


    print(f'#{test_case} {ans}')