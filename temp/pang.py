import sys
sys.stdin = open("pang.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    garu_arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    sum_pang = 0

    for i in range(N):
        for j in range(M):
            sum_pang = garu_arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    sum_pang += garu_arr[ni][nj]
            max_v = max(sum_pang, max_v)
    print(f'#{test_case} {max_v}')
