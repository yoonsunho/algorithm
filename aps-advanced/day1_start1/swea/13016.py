import sys
sys.stdin = open("txt/13016.txt", "r")

# 16진수 -> 2진수

def hex_to_dec(hex_num):
    hex_digit ='0123456789ABCDEF'
    dec_num = [0] * n

    for i in range(len(hex_num)):

        dec_num[i] = hex_digit.index(hex_num[i])

    return dec_num

def dec_to_bin(dec_num):
    str1 = ''
    while dec_num > 0:
        remain = dec_num % 2
        str1 = str(remain) + str1
        dec_num //= 2

    if len(str1) < 4:
        str1 = '0'*(4-len(str1)) + str1
    return str1

T = int(input())
for tc in range(1, T+1):

    n, hex_num = input().split()
    n = int(n)

    dec = hex_to_dec(hex_num)
    # print(dec)

    ans = ''
    for d in dec:
        ans += dec_to_bin(d)



    print(f'#{tc} {ans}')