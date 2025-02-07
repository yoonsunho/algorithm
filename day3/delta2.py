N = 2
M = 3
for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)

# 델타 응용
# N x N 배열애서 각 원소를 중심으로, 상하좌우 k 칸의 합계 중 최댓값(k=2)
arr = [list(map(int,input().split())) for _ in range(N)]

max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for c in range(1,k+1):
                ni, nj = i + di * c, j + di * c
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s

# 전치 행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    # 3x3행렬
# 방법1
for i in range(3):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 방법2
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]