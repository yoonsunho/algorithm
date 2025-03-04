import sys
sys.stdin = open('ladder1.txt')

dxy = [[1, 0], [0, 1], [0, -1]]  # 아래, 오른쪽, 왼쪽
# 사다리를 타고 내려가는 함수
# x, y는 시작 좌표
def search_ladder(x, y):
    # 방문 여부를 확인하기 위한 변수가 필요하다
    # 이건 원본을 똑같이 복사할 거다. 왜냐? 원본을 훼손하면 안된다
    # 다른 시작점에 영향을 끼치지 않도록 하기 위해서
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1  # 초기 시작 위치 방문했다고 치자.

    # 이제부터 쭉죽 내려갑니다.
    # 언제까지 ? x: 행, y: 열
    # 행이 99, 마지막줄에 도달할 때까지 반복한다.
    while x != 99:
        for dx, dy in dxy:
            # nx, ny는 다음에 이동할 좌표 !
            nx, ny = x + dx, y + dy

            """
            이동하기 위한 조건 
            1. 범위 안에 들어야한다.
            2. 사다리가 놓여있어야 한다.
            3. 방문한 적이 없어야 한다. 
            """
            # 범위를 벗어난 경우에는 탐색하지 않겠다.
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 사다리가 놓여있지 않은 경우
            if not data[nx][ny]:
                continue

            # 방문한 적이 있다면 스킵
            if visited[nx][ny]:
                continue

            # 방문할 수 있는 경우
            visited[nx][ny] = 1
            x , y = nx, ny

    return data[x][y] == 2  # 제대로 도착했으면 True, 아니면 False


for _ in range(1, 11):
    tc = int(input())
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]
    result = -1  # 시작점 인덱스를 저장할 변수

    # 출발점을 찾아야한다.
    # 1행에서 "1" 인 친구들을 시작점으로 한다.
    # 열을 끝까지 탐색하는 거에요.
    for j in range(N):
        # 사다리가 놓여있지 않으면 skip
        if data[0][j] == 0:
            continue
        # 사다리 타는 코드를 작성하자.
        # 시작점을 주고, 만약에 2에 도착한다면 True, 그 외는 False
        if search_ladder(0, j):
            # 2에 도착했다면, 현재 j 인덱스가 결과에 도달하기 위한 시작점
            result = j
            break

    print(f'#{tc} {result}')
