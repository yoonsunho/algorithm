import sys
sys.stdin = open("txt/1211.txt", "r")

def going_down(i,j):
    x, y = i, j
    count = 0
    while True:
        i += 1
        if j <= 98 and ladder[x][j+1] == 1:
            k = 1
            while ladder[x][j+k] == 1:
                count += 1
                if j + k <= 99:
                    k += 1
                else:
                    break
        elif j >= 1 and ladder[x][j-1] == 1:
            k = 1
            while ladder[x][j-k] == 1:
                count += 1
                if j - k >= 0:
                    k += 1
                else:
                    break

        if i == 98:
            break

    return count


for _ in range(10):

    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    # print(ladder)
    st = []

    for j in range(100):
        if ladder[0][j] == 1:
            st.append(j)

    n = len(st)
    count = [0] * n

    for i in range(n):
        count[i] = going_down(0,st[i])

    print(count)


    # print(st)


    print(f'#{tc}')