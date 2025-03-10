import sys
sys.stdin = open("txt/5656.txt", "r")
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def shoot(cnt, remains, now_matrix):    # 구슬 굴린 횟수 남은 벽돌 수, 현재 벽돌 메트릭스

    global min_blocks

    if cnt == N or remains == 0:    # 구슬을 모두 발사 or 남은 벽돌 없을 때
        min_blocks = min(min_blocks, remains)
        return 
    
    # 한 줄 씩 떨구기
    # 구슬을 쏘는 열에서 가장 위를 찾기
    for col in range(W):    # 이게 dfs인듯 (모든 경우 살펴보기)

        copy_matrix = [row[:] for row in now_matrix]
        
        row = -1
        for r in range(H):
            if copy_matrix[r][col]: # 벽돌이 있으면
                row = r
                break
        if row == -1:   # 벽돌이 없는 열이면 다음 열 확인하기
            continue
            
        # 깨질 벽돌들을 리스트에 담기
        # 행, 열, 숫자
        q = deque([[row, col, copy_matrix[row][col]]])
        now_remains = remains - 1   # 남은 벽돌 수 를 계산할 변수
        copy_matrix[row][col] = 0   # 구슬이 처음 만나는 벽돌자리
        
        # 주변 벽돌들 깨짐
        while q:
            r, c, p = q.popleft()
            for k in range(1,p):    # 숫자마늠 반복하면서 벽돌 깨짐
                for i in range(4):
                    ni = r + (di[i]*k)
                    nj = c + (dj[i]*k)

                    if ni < 0 or ni >= H or nj < 0 or nj >= W:  # 범위 밖이면
                        continue

                    if copy_matrix[ni][nj] == 0:    # 벽돌이 없으면
                        continue

                    q.append([ni,nj,copy_matrix[ni][nj]])   # 다음 벽돌 추가
                    copy_matrix[ni][nj] = 0 # 벽돌 깨짐
                    now_remains -= 1    # 남은 벽돌 수 감소

        # 터지고 난 후 빈칸 메꾸기 (swap)
        for c in range(W):
            idx = H - 1  # 벽돌이 위치할  index
            for r in range(H-1, -1, -1):
                if copy_matrix[r][c]:
                    copy_matrix[r][c], copy_matrix[idx][c] = copy_matrix[idx][c], copy_matrix[r][c]
                    idx -= 1

        shoot(cnt + 1, now_remains, copy_matrix)


                
    
    
    
T = int(input())
for tc in range(1, T+1):

    N, W, H = map(int, input().split())     # N : 구슬 던지는 횟수, 가로, 세로(1 ≤ N ≤ 4,2 ≤ W ≤ 12,2 ≤ H ≤ 15)

    matrix = [list(map(int, input().split())) for _ in range(H)]    # 쌓여있는 벽돌 메트릭스

    min_blocks = 1e9    # 남은 최소 벽돌의 수를 담을 변수
    blocks = 0 # 남은 벽돌의 수를 담을 변수

    #현재 벽돌 수 계산
    for row in matrix:
        for el in row:
            if el:  # 벽돌이 있으면
                blocks += 1
                
    shoot(0, blocks, matrix)

    print(f'#{tc} {min_blocks}')