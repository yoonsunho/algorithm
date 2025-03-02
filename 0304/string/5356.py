import sys
sys.stdin = open("txt/5356.txt", "r")

# 못품

T = int(input())
for tc in range(1, T+1):

    matrix = [list(input()) for _ in range(5)]

    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(matrix[i]))

    for i in range(5):
        if len(matrix[i]) < max_len:
            for j in range(max_len-len(matrix[i])):
                matrix[i].append("")

    matrix2 = list(map(list, zip(*matrix)))



    print(f'#{tc}',end=" ")
    for i in range(max_len):
        for j in range(5):
            print(matrix2[i][j],end="")
    print()


