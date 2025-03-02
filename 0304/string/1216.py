import sys
sys.stdin = open("txt/1216.txt", "r")



for _ in range(1,11):
    T = int(input())

    matrix = [list(input()) for _ in range(100)]

    ans = 1
    k = 100     # 회문의 최대 길이
    for _ in range(2):
        for i in range(100):
            for j in range(100 - k + 1):
                for l in range(k//2):
                    if matrix[i][j+l] == matrix[i][j+k-1-l]:
                        ans = k
                        break
            else:
                k -= 1
                break



        matrix = list(map(list, zip(*matrix)))


    print(f'#{T} {ans}')