# 케슬 디팬스(골드3)
# 0421(월)

# gpt참조
# BFS
from collections import deque
import copy

def max_kill(j_list):
    kills = 0
    new_matrix = copy.deepcopy(matrix)
    for _ in range(N):
        targets = set()
        for x in j_list:
            q = deque([(N-1, x, 1)])    # 궁수의 바로 위점을 시작점으로 데큐넣기
            visited = [[0] * M for _ in range(N)]

            while q:
                i, j, d = q.popleft()   # 좌표, 이동 거리
                if d > D:
                    continue
                if new_matrix[i][j] == 1:
                    targets.add((i, j))
                    break

                for di, dj in [[0, -1], [-1, 0], [0, 1]]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni <N and 0 <= nj < M and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append((ni, nj, d+1))
        for i, j in targets:
            new_matrix[i][j] = 0
            kills += 1
        new_matrix.pop()
        new_matrix.insert(0,[0]*M)      # 첫줄에 0채우기 => 적의 이동 효과
    # print(kills)
    return kills


def comb(cnt, st):

    global max_v

    if cnt == 3:
        # print(j)
        kill = max_kill(j_li)
        max_v = max(max_v, kill)
        return

    for i in range(st, M):
        if visited[i]:
            continue

        visited[i] = 1
        j_li.append(i)
        comb(cnt+1, i+1)
        visited[i] = 0
        j_li.pop()

N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * M
j_li = []      #

max_v = 0   # 죽인 적의 최대 수 를 담을 변수
comb(0, 0)
print(max_v)
