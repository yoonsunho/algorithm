import sys
sys.stdin = open("txt/ladder.txt", "r")

for _ in range(10):
    T = int(input())

    ladder_arr = [list(map(int,input().split())) for _ in range(100)]

    st_i = 99
    st_j = 0

    for i in range(100):
        if ladder_arr[99][i] == 2:
            st_j = i

    while st_i > 0:
        if 0 <= st_j+1 <= 99 and ladder_arr[st_i][st_j+1] == 1:
            while ladder_arr[st_i][st_j + 1] > 0:
                if st_j <= 98:
                    st_j += 1
                else:
                    st_j = 99
        elif 1 <= st_j-1 <= 99 and ladder_arr[st_i][st_j-1] == 1:
            while ladder_arr[st_i][st_j - 1] > 0:
                if st_j >= 0:
                    st_j -= 1
                else:
                    st_j = 0
        st_i -= 1



    print(f'#{T} {st_j}')