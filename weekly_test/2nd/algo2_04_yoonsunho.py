'''
2
3
0000000000
0000001000
0000000000
0002000000
0000000000
0000000000
0000003000
0000000000
0000000000
0000000000
8
0000000000
0020000000
0000030000
0000000200
0010000000
0000000000
0000200000
0304000030
0400000010
0000000000

#1 73
#2 42
'''

T = int(input())    # 1<=T<=10
for tc in range(1, T+1):

    N = int(input())        # RGB괴물의 수 (1<=N<=100)
    matrix = [list(map(int, input())) for _ in range(10)]
    # print(matrix)

    monster_i =[]
    monster_j = []
    for i in range(10):
        for j in range(10):
            if matrix[i][j] != 0:
                monster_i.append(i)
                monster_j.append((j))
    print(monster_i,monster_j)

    for i in range(10):
        for j in range(10):
            if matrix[i][j] != 0:
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    for k in range(1, matrix[i][j]+1): # k = 1 ~ matrix[i][j]까지
                        ni = i + di * k
                        nj = j + dj * k
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            if matrix[ni][nj] != 4:
                                matrix[ni][nj] += 1


    count = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 0:
                count += 1

    print(f'#{tc} {count}')