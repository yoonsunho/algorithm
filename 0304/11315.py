import sys
sys.stdin = open("txt/11315.txt","r")

# 50m
# 배열 할 떄 i, j 계속 실수로 잘못쓰는거 잡으려고 노력하기!!

T = int(input())

for tc in range(1,T+1):

    N = int(input())

    omok = [list(input()) for _ in range(N)]
    # print(omok)

    ans = "NO"

    # 가로, 세로 검사
    for _ in range(2):
        for i in range(N):
            for j in range(N-4):
                if omok[i][j] == "o":
                    count = 1
                    for k in range(1, 5):
                        if omok[i][j+k] == "o":
                            count += 1
                        if count >= 5:
                            ans = "YES"
                            break

        omok = list(zip(*omok))
        # print(omok)

    # 원상복귀는 굳이 안해도 될듯..
    # 대각선 검사(정방향)
    for i in range(N-4):
        for j in range(N-4):
            if omok[i][j] == "o":
                count = 1
                for k in range(1,5):
                    if omok[i+k][j+k]== "o":
                        count += 1
                if count >= 5:
                    ans = "YES"
                    break

    new_omok = [[0]*N for _ in range(N)]


    # 배열 데칼코마니
    for i in range(N):
        for j in range(N):
            new_omok[i][j] = omok[i][N-j-1]

    # print(omok)
    # print(new_omok)
    for i in range(N-4):
        for j in range(N-4):
            if new_omok[i][j] == "o":
                count = 1
                for k in range(1, 5):
                    if new_omok[i+k][j+k] == "o":
                        count += 1
                if count >= 5:
                    ans = "YES"
                    break



    print(f'#{tc} {ans}')