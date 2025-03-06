import sys
sys.stdin = open("txt/13017.txt", "r")

# 10진수 -> 2진수

def decimal_to_binary(target):

    pow = -1
    binary_number = ''

    # for i in range(12):
    while pow > -13:
        if target >= 2 ** pow:
            target -= 2**pow
            binary_number += '1'
        else:
            binary_number += '0'

        if target == 0:
            break

        pow -= 1

    if target == 0:
        return binary_number
    else:
        return 'overflow'

T = int(input())
for tc in range(1, T+1):

    N = float(input())

    ans = decimal_to_binary(N)


    print(f'#{tc} {ans}')