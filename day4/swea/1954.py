import sys
sys.stdin = open("txt/1954.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for j in range(N):
        arr[0][j] = j+1

    for i in range(N):
        arr[i][N-1] = N+i

    for i in range(N):
        arr[N-1][i] = 3*N-2-i

    for i in range(1,N):
        arr[]





    for i in range(N):
        print(*arr[i])

    # for i in range(N):

    print(f'#{test_case}')