import sys
sys.stdin = open("txt/pang2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    pung_list = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            pung_sum = pung_list[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for k in range(1, pung_list[i][j]+1):
                    ni = i + di * k
                    nj = j + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        pung_sum += pung_list[ni][nj]

            max_v = max(max_v, pung_sum)



    print(f'#{test_case} {max_v}')