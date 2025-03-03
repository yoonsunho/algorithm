import sys
sys.stdin = open("txt/11315.txt","r")

T = int(input())
for tc in range(1,T+1):

    N = int(input())        # N*N 배열

    omok = [list(input()) for _ in range(N)]

    ans = "NO"
    # 가로 세로
    for _ in range(2):
        for i in range(N):
            for j in range(N-5+1):
                if omok[i][j] == "o":
                    for k in range(1,5):
                        if omok[i][j+k] != "o":
                            break
                        else:
                            ans = "YES"

    # 대각선(정)


        omok = list(map(list,zip(*omok)))

    print(f'#{tc} {ans}')