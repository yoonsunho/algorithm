import sys
sys.stdin = open("txt/1953.txt", "r")
from collections import deque

# 1. BFS 로 접근
# - 이동 방향 : 상하좌우
# - 이동이 불가능한 케이스
#   - [델타 배열 기본] 범위밖으로 나가면 못감
#   - [방문 기록 기본] 이미 방문한 곳은 안감
#   - [문제 조건]
#       - 현재 내 위치에서 이동할
#
#
# 2. 방문 기록을 해야한다 (visited)

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라 이동 가능 여부
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R,C):
    dq = deque([[R, C]])    # 후보군
    visited[R][C] = 1   # 출발점 초기화

    while dq:
        nowy, nowx = dq.popleft()
        dirs = types[graph[nowy][nowx]]     # 터널이 뚫린 위치를 알려줌
        
        for i in range(4):  # 4방향을 확인하면서

            if dirs[i] == 0:        # 출구가안열려 있는 경우 continue
                continue

            new_y = nowy + dy[i]
            new_x = nowx + dx[i]

            # 범위 밖으로 넘어가면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue
            
            # 이미 방문 했다면 pass
            if visited[new_y][new_x]:
                continue

            # 못가면 pass (그곳에 터널이 없으면)
            if graph[new_y][new_x] == 0:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]
            
            # 현재 상좌 -> next_dirs가 하우 안뚫렸으면 못감
            if i % 2 == 0 and next_dirs[i+1] == 0:
                continue

            # 현재 하우 -> next_dirs가 상좌 안뚫렸으면 못감
            if i % 2 == 1 and next_dirs[i-1] == 0:
                continue

            # L 시간이 넘어가면 볼 필요 없다 (시간 단축 가능)
            if visited[nowy][nowx] + 1 > L:
                continue
            
            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[nowy][nowx] + 1
            dq.append([new_y, new_x])


T = int(input())
for tc in range(1, T+1):
    
    # 다섯개의 변수가 각각의 의미를 가지고 있다
    # -> 리스트를 안만드는게 더 편하다
    N, M, R, C, L = map(int, input().split())   # 높이, 가로, 맨홀의 세로, 맨홀의 가로, 소요시간

    graph = [list(map(int,input().split())) for _ in range(N)]      # 터널의 정보가 들어있는 matrix

    visited = [[0] * M for _ in range(N)]       # 특정 좌표까지 몊시간 걸렸는지 기록 (bfs로 풀기 위한 준비)

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')