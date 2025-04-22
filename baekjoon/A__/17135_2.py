# 다시 풀어보기
import copy
from collections import deque

def bfs(anc_list):

    killed = 0
    new_matrix = copy.deepcopy(matrix)

    for _ in range(N):
        targets = set()     # 적수 이동할 떄마다 target은 초기화 하고 다시 카운ㄷ트
        for x in anc_list:
            q = deque([(N-1, x, 1)])      # 현재 궁수 위치의 바로 위 지점을 기준으로 탐색 시작
            visited = [[0]*M for _ in range(N)]

            while q:
                i, j, d = q.popleft()

                if d > D:
                    continue

                if new_matrix[i][j] == 1:
                    targets.add((i, j))
                    break

                for di, dj in [[0, -1], [-1, 0], [0, 1]]:   # 여기부터 모두 거리는 동일하므로 우선순위인 왼쪽 부터 탐색 시작
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append((ni, nj, d+1))

        for i, j in targets:
            new_matrix[i][j] = 0
            killed += 1
        new_matrix.pop()
        new_matrix.insert(0, [0]*M)

    return killed

def anchors_idx(cnt, st):

    global max_v

    if cnt == 3:
        # print(anchors)
        kill = bfs(anchors)
        max_v = max(max_v, kill)
        return

    for i in range(st, M):
        anchors.append(i)
        anchors_idx(cnt+1, i+1)
        anchors.pop()



N, M, D = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]  # 적군들의 정보를 담을 메트릭스

max_v = 0   # 제거할 수 이쓴 적의 최대 수를 담을 변수

anchors = []    # 궁수들의 j 좌표를 담을 리스트
anchors_idx(0, 0)
print(max_v)