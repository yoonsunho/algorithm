import sys
sys.stdin = open("txt/coloring.txt", "r")

T = int(input())    # 1<= T <= 50
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 2 <= N <= 30

    col_area = [list(map(int,input().split())) for _ in range(N)]

    for color in col_area:
        if col_area[5] ==1:
            pass
    print(f'{test_case}')