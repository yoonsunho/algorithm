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

    for i in range(99):
        st_i -= 1
        if 0 <= st_j-1 <= 99 and ladder_arr[98-i][st_j-1] == 1:
            st_j -= 1
            while ladder_arr[st_i-1][st]
        elif 0 <= st_j+1 <= 99 and ladder_arr[98-i][st_j+1] == 1:
            st_j += 1
        if st_i == 0:
            break





    print(f'#{T} {st_j}')