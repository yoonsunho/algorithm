import sys
sys.stdin = open("txt/1861.txt", "r")

# 정사각형 방 정답 코드
# 접근 법
# N * N visited 배열을 만든다
# 해당 숫자에서 갈 수 있다면 1을 기록한다
# 연속된 1의 길이가 가장 긴 곳이 정답
# 같은 길이가 있다면, 작승 수가 정답 위치

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    room = [list(map(int,input().split())) for _ in range(N)]

    visited = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            for x in range(4):
                ni, nj = i + di[x], j + dj[x]
                if 0 <= ni < N and 0 <= nj < N:
                    if room[ni][nj] == room[i][j] + 1:
                        visited[room[i][j]] = 1
                        break   # 갈 수 있는곳은 어짜피 하나밖에 없기 때문에 찾았으면 바로 종료
    # print(visited)
    
    # 연속한 1의 최대 개수 구하기  + 최대개수를 보유한 최소 인덱스 구하기
    min_idx = 0      # 최소 인덱스를 담을 변수
    max_cnt = 0     # 연속한 1의 최대 개수를 담을 변수
    cnt = 0

    for i in range(N*N+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                min_idx = i - cnt   # 현재 i 에는 1을 만나다가 만난 0의 인덱스(첫 지점이 아닌 끝점 +1값임)
                max_cnt = cnt
            cnt = 0

    print(f'#{tc} {min_idx} {max_cnt+1}')