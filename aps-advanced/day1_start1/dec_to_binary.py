target = 74     # 10진수

# print(bin(74))  # 2진수 변환
# print(hex(74))  # 16진수 변환

def dec_to_binary(target):
    binary_number = ''

    while target >0:
        remain = target % 2     # 2로 나눈 나머지
        binary_number = str(remain) + binary_number
        target = target // 2   # 2 로 나눈다
    print(binary_number)

dec_to_binary(target)       # 1001010

def binary_to_decimal(binary_str):
    # 1. binary_str 문자열 뒤에서 부터 진행
    # 2. 각 자리에 맞는 수를 곱하면서, 결과에 더한다
    decimal_number = 0
    pow = 0     # 지수

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_number += 2 ** pow
        #     pow += 1
        # else:
        pow += 1
    print(decimal_number)

binary_to_decimal("1001010")        # 74


# 10진수 -> 16 진수
def decimal_to_hexadcimal(target):
    hex_digit = '0123456789ABCDEF'
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16
    print(hex_number)


decimal_to_hexadcimal(160)  # A0