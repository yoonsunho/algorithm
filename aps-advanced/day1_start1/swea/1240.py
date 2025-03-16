import sys
sys.stdin = open("txt/1240.txt", "r")

code_dict = {'1011000': 0, '1001100': 1, '1100100': 2, '1011110': 3, '1100010': 4, '1000110': 5, '1111010': 6, '1101110': 7, '1110110': 8,'1101000': 9}

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())    # 세로, 가로(1<=N <= 50, 56 <= M <= 100)

    matrix = [input() for _ in range(N)]
    # print(matrix)
    st_i, st_j = -1, -1

    code_list = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            # print(matrix[i][j], end='')
            if matrix[i][j] == '1':
                st_i, st_j = i, j
                break
        # print(st_idx)

    for j in range(st_j, st_j-56, -7):
        code_list.append(matrix[st_i][j:j-7:-1])

    # print(code_list)

    sum_v = 0
    for i in range(8):
        code_list[i] = code_dict[code_list[i]]
        sum_v += code_list[i]
    # print(code_list)
    # print((code_list[0]+code_list[2]+code_list[4]+code_list[6])*3 + (code_list[1]+code_list[3]+code_list[5]+code_list[7]))

    if ((code_list[1]+code_list[3]+code_list[5]+code_list[7])*3 + (code_list[0]+code_list[2]+code_list[4]+code_list[6])) % 10 != 0:
        sum_v = 0

    print(f'#{tc} {sum_v}')