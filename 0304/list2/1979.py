import sys
sys.stdin = open("txt/1979.txt","r")

# 어디에 단어
# 48m
# 좀 오래 걸렸지만 혼자 풀긴함

def check(x,y,k):
    cnt = 1
    if y + k == N or arr[x][y + k] == 0:   # j 가 마지막 인덱스 이거나 다음칸이 0 일 때
        for a in range(1, k):
            if arr[x][y+a] == 1:
                cnt += 1
    if cnt == K:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())         # 5 ≤ N ≤ 15, 2 ≤ K ≤ N

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for _ in range(2):  # 가로 , 세로 실행
        for i in range(N):
            for j in range(N-K+1):
                if arr[i][j] == 1 and (j == 0 or arr[i][j-1] == 0):
                    ans += check(i, j, K)
        arr = list(map(list, zip(*arr)))


    print(f'#{tc} {ans}')