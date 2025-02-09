import sys
sys.stdin = open("txt/where.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 가로 세로 길이 N, 단어의 길이 K
    N, K = map(int, input().split())    # 5<=N<=15, 2<=K<=N

    # 퍼즐의 모양(흰 :1, 검:0)
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if count - K >= 0:
                count -= (K - 1)
                max_v += count
            else:
                count = 0



    print(f'#{test_case} {max_v}')