import sys
sys.stdin = open("txt/1961.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # N x N행렬(3<=N<= 7)
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr_90_degree = [[0] * N for _ in range(N)]
    arr_180_degree = [[0] * N for _ in range(N)]
    arr_270_degree = [[0] * N for _ in range(N)]

    # 90도 회전
    for i in range(N):
        for j in range(N):
            arr_90_degree[i][j] = arr[N-j-1][i]
    # print(arr_90_degree)

    # 180 도 회전
    for i in range(N):
        for j in range(N):
            arr_180_degree[i][j] = arr[N-i-1][N-j-1]
    # print(arr_180_degree)


    # 270도 회전
    for i in range(N):
        for j in range(N):
            arr_270_degree[i][j] = arr[j][N-i-1]
    # print(arr_270_degree)

    print(f'#{test_case}')
    for i in range(N):
        print(f'{"".join(map(str,arr_90_degree[i]))} {"".join(map(str,arr_180_degree[i]))} {"".join(map(str,arr_270_degree[i]))}' )

