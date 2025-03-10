import sys
from itertools import combinations
sys.stdin = open("txt/10580.txt", "r")

# 시작점이 더 크고 끝점이 더 낮은 경우 고려 안함

def check(check_list):
    # print(check_list)
    count = 0
    if check_list[0][0] < check_list[1][0] and check_list[0][1] > check_list[1][1]:
        count += 1
       
    # 이 부분 고려 안해서 처음에 틀림
    elif check_list[0][0] > check_list[1][0] and check_list[0][1] < check_list[1][1]:
        count += 1

    # print(count)
    return count

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    hei_matrix = [[0]*2 for _ in range(N)]

    for i in range(N):

        hei_matrix[i][0], hei_matrix[i][1] = map(int,input().split())

    # print(hei_matrix)
    cnt = 0
    for i in combinations(hei_matrix, 2):
        cnt += check(list(i))

    print(f'#{tc} {cnt}')
