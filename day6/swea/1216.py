import sys
sys.stdin = open("txt/1216.txt", "r")
# 내 실패한 코드

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):

    T = int(input())

    ABC_list = [list(input()) for _ in range(100)]
    # print(ABC_list)

    max_v = 1  # 가장 긴 회문의 길이를 담을 변수
    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(j+1, 100):
                for ll in range((k - j) // 2):
                    if ABC_list[i][j + ll] != ABC_list[i][k - ll]:
                        print(j+ll, k-ll)
                        break
                else:
                    max_len = k - j + 1
                max_v = max(max_v, max_len)
    print(max_v,end=' ')

    # for i in range(100):
    #     for j in range(100):
    #         for k in range(99, j, -1):
    #             for ll in range((k - j) // 2):
    #                 if ABC_list[i][j + ll] != ABC_list[i][k - ll]:
    #                     break
    #             else:
    #                 max_len = k - j + 1
    #                 max_v = max(max_v, max_len)
    # print(max_v,end=' ')    # 17 18 18 20 18 18 18 18 18 17

    # 세로
    for j in range(100):
        for i in range(100):
            for k in range(i+1, 100):
                for ll in range((k - i) // 2):
                    if ABC_list[i+ll][j] != ABC_list[k-ll][j]:
                        break
                else:
                    max_len = k - i + 1
                max_v = max(max_v, max_len)
    print(max_v, end=' ')   # 18 18 16 16 20 21 18 18 17 18

    print(f'#{T} {max_v}')
