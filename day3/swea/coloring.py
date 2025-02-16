import sys
sys.stdin = open("txt/coloring.txt", "r")

T = int(input())    # 1<= T <= 50
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 2 <= N <= 30(영역의 개수)
    new_arr = [[0] * 10 for _ in range(10)]
    purple_num = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                new_arr[i][j] += color

                if new_arr[i][j] == 3:
                    purple_num += 1

    print(f'#{test_case} {purple_num}')