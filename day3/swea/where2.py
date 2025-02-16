import sys
sys.stdin = open("txt/where.txt", "r")



# 글자가 들어갈 수 있는지 여부를 알 수 있는 함수
def check(i,j):     # 탐색을 시작할 좌표 전달 받음
    count = 0
    for x in range(K):
        if arr[i][j+x] == 1:
            count += 1
    # !!!!!주의: or 문 쓸떄 순서 주의 !! 먼저 써야할 게 뭔지 먼저 체크해보기!!
    if count == K and (j+K == N or arr[i][j+K] == 0):   # 다음 인덱스에 있는 값이 0 이거나 마지막 1 이 배열의 끝인 경우
        return 1
    else:
        return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 가로 세로 길이 N, 단어의 길이 K
    N, K = map(int, input().split())    # 5<=N<=15, 2<=K<=N

    # 퍼즐의 모양(흰 :1, 검:0) (1 에 글자가 올 수 있음)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 조건을 만족하는 자리의 개수를 담을 변수
    cnt = 0

    for _ in range(2):
        for i in range(N):
            for j in range(N-K+1):
                # 만약 1이 배열이 첫번째 1 인경우이거나 , 이전 값이 0
                if arr[i][j] == 1 and (j == 0 or arr[i][j-1] == 0):
                    cnt += check(i, j)
        arr = list(map(list, zip(*arr)))


    print(f'#{test_case} {cnt} ')