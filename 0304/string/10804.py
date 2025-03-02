import sys
sys.stdin = open("txt/10804.txt", "r")

# 9m

T = int(input())
for tc in range(1, T+1):

    str1 = input()

    N = len(str1)
    str2 = list(str1[::-1])
    # print(str1)
    # print(str2)
    for i in range(N):
        if str2[i] == "p":
            str2[i] = 'q'
        elif str2[i] == "q":
            str2[i] = 'p'
        elif str2[i] == "b":
            str2[i] = 'd'
        elif str2[i] == "d":
            str2[i] = 'b'



    print(f'#{tc} {"".join(str2)}')