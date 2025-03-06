import sys
sys.stdin = open("txt/23888.txt", "r")

# 2진수 -> 10진수

T = int(input())
for tc in range(1, T+1):

    N = int(input())        # 문자열의 개수
    M = int(N*10/7)
    arr = [0] * M
    str1 = ''

    for _ in range(N):
        str1 += input().strip()
    # print(str1)


    for i in range(M):
        binary_number = str1[i*7:i*7+7]        # 10자리씩 끊어서 받기
        # print(binary_number)
        pow = 0
        decimal_number = 0

        # n = len(binary_number)
        for x in reversed(binary_number):
            if x == "1":
                decimal_number += 2 ** pow

            pow += 1

        arr[i] = decimal_number


    # print(arr)
    print(f'#{tc} {" ".join(map(str,arr))}')