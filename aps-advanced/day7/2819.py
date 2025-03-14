import sys
sys.stdin = open("txt/2819.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
#
def recur(i,j,cnt,num_str):

    if cnt == 7:
        num_arr.add(num_str)
        return

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if 0 <= ni < 4 and 0 <= nj < 4:
            # num + str(matrix[ni][nj])
            # print(num)
            recur(ni, nj, cnt+1, num_str + str(matrix[ni][nj]))
            # num - str(matrix[ni][nj])

T = int(input())

for tc in range(1, T+1):

    matrix = [list(map(int, input().split())) for _ in range(4)]

    num = ''
    num_arr = set()
    for i in range(4):
        for j in range(4):
            recur(i, j, 1, str(matrix[i][j]))

    # print(num_arr)

    print(f'#{tc} {len(num_arr)}')