import sys
sys.stdin = open("txt/ladder.txt", "r")

#사다리를 타고 내려가는 함수
# s,y 는 시작좌표
def search_ladder(x,y):
    # 방문 여부를 확인하기 위한 변수 필요
    # 이건 원본을 똑같이 복사할것임
    # 다른 시작점에 영향을 끼치지 않도록 하기 위해서
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1   # 초기 시작 위치 방문했다 치자.

    # 이제부터 쭉쭉 내려감
    # 언재까지? x: 행, y: 열
    # 행이 99, 마지막줄 도달할 때까지 반복
    while x != 99:
        for dx, dy in dxy:


for _ in range(1,11):
    
    tc = int(input())
    N = 100
    data = [list(map(int,input().split())) for _ in range(N)]
    result = -1     # 시작점 인덱스를 저장할 변수
    
    # 출발 점을 찾아야 함
    # 1행에서 "1"인 친구들을 시작점으로 한다
    # 열을 끝까지 탐색
    for j in range(N):
        # 1행에서 데이터가 1인 친구(시작점)으로 할 친구들 산정
        if data[0][j] ==1:
            
            