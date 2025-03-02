import sys
sys.stdin = open("txt/1215.txt","r")

for tc in range(1, 11):

    N = int(input())

    matrix = [list(input()) for _ in range(8)]


    count = 0
    for _ in range(2):
        for i in range(8):
            for j in range(8-N+1):
                for k in range(N//2):
                    if matrix[i][j+k] != matrix[i][j+N-1-k]:
                        break
                else:
                    count += 1
        matrix = list(map(list, zip(*matrix)))


    print(f'#{tc} {count}')