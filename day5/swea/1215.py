import sys
sys.stdin = open("txt/1215.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    str_list = [list(input().split()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(9-N):
            for k in range(N//2):
                if str_list[i][j+k] != str_list[i][j+N-1-k]:
                    print(str_list[i][j+k])
                    break
            else:
                cnt += 1

    # for i in range(9):
    #     for j in range(9-N):
    #         for k in range(N//2):
    #             if str_list[i+k][j] != str_list[i-k+N-1][j]:
    #                 break
    #             else:
    #                 cnt += 1

    print(f'#{test_case} {cnt}')