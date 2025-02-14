import sys
sys.stdin = open("txt/where.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 가로 세로 길이 N, 단어의 길이 K
    N, K = map(int, input().split())    # 5<=N<=15, 2<=K<=N

    # 퍼즐의 모양(흰 :1, 검:0) (1 에 글자가 올 수 있음)
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    new_list = [[0]*(N+2) for _ in range(N+2) ]
    # print(new_list)
    for i in range(1,N+1):
        for j in range(1,N+1):
            new_list[i][j]= arr[i-1][j-1]
    print(new_list)

    find_list = [0]+[1]*K +[0]

    for i in range(N+2):
        for j in range(N-K+2):
            # print(new_list[i][j:j+K+2])
            if new_list[i][j:j+K+3] == find_list:
                cnt += 1

    rotate_new_list = list(zip(*new_list[::-1]))


    for i in range(N+2):
        for j in range(N-K+2):
            # print(new_list[i][j:j+5])
            if rotate_new_list[i][j:j+K+3] == find_list:
                cnt += 1



    print(f'#{test_case} {cnt} ')