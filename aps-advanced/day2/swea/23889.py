import sys
sys.stdin = open('txt/23889.txt', "r")

# 16진수 -> 10진수
# 16진수 -> 2 진수 -> 10진순

def hex_to_bin(num):
    hex_digit = '0123456789ABCDEF'
    n = len(num)
    dec = [0] * n
    for i in range(n):
        dec[i] = hex_digit.index(num[i])
    return dec

def dec_to_bin(num):

    str1 = ''

    while num > 0:
        remain = num % 2
        str1 = str(remain) + str1
        num //= 2

    n = len(str1)

    if n < 4:
        str1 = '0'*(4-n) + str1
    return str1

def bin_to_dec(num):
    # print(reversed(num))
    pow = len(num)-1
    dec_num = 0
    for n in num:
        dec_num += int(n) * 2**pow
        pow -= 1
    return dec_num

T = int(input())

for tc in range(1, T+1):

    hexa_num = input()
    dec = hex_to_bin(hexa_num)

    # print(dec)
    bin_str = ''

    for d in dec:
        bin_str += dec_to_bin(d)    # 2진수로 변환

    N = len(dec)
    ans = [0] * ((N*4)//7 + 1)
    for i in range(N*4//7):
        bin_arr = bin_str[i*7: i*7+7]
        ans[i] = bin_to_dec(bin_arr)

    last_n = bin_str[(N*4//7)*7:]
    # print(last_n)
    ans[N*4//7] = bin_to_dec(last_n)

    # print(bin_str)
    # print(ans)
    print(f'#{tc} {" ".join(map(str,ans))}')


