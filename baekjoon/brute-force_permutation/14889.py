# 0405(토)
# 스타트와 링크(실버1)
# 굳이 링크팀ㅁ 스타트 팀 이름 다르게 한 이유가 뭘까 함정인가 .. 굳이 나눌 필요는 없어 보임
import sys
input = sys.stdin.readline

def find_min(silver, link):

    global min_v
    sil_cnt = 0
    link_cnt = 0
    for i in silver:
        for j in silver:
            sil_cnt += matrix[i][j]

    for i in link:
        for j in link:
            link_cnt += matrix[i][j]

    min_v = min(min_v, abs(sil_cnt-link_cnt))


def dfs(cnt,st):
    global silver_team

    if cnt == N//2:
        link_team =[]
        for i in range(N):
            if i not in silver_team:
                link_team.append(i)

        find_min(silver_team, link_team)
        return

    for i in range(st, N):
        if visited[i]:
            continue
        visited[i] = 1
        silver_team.append(i)
        dfs(cnt+1, i+1)
        visited[i] = 0
        silver_team.pop()


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

team = [i for i in range(N)]
silver_team = []

visited = [0] * N

min_v = float('inf')
dfs(0,0)

print(min_v)
