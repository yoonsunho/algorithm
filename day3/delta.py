di = [0, 1, 0, -1]     # 오른쪽 부터 시계 방향으로
dj = [1, 0, -1, 0]

# # i = 2
# # j = 3
# for dir in range(4):
#     ni = i + di[dir]
#     nj = j + dj[dir]
#     print(ni,nj)

'''
2 4
3 3
2 2
1 3
'''
N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < M:   # 존재하지 않는 음수 인덱스 제거를 위함
                print(ni, nj)
'''
0 1
1 0
0 2
1 1
0 0
1 2
0 1
1 1
0 0
1 2
1 0
0 1
1 1
0 2
'''