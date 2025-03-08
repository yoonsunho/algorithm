import sys
sys.stdin = open("txt/23890.txt", "r")

def dec_to_bin(num):
    bin_str = ''
    while num > 0:
        remain = num % 2
        bin_str = str(remain) + bin_str
        num //= 2

    if len(bin_str) < 4:
        bin_str = '0'*(4-len(bin_str)) + bin_str

    return bin_str


T = int(input())
for tc in range(1, T+1):

    hex_list = list(input().strip())
    # print(hex_list)
    n = len(hex_list)

    hex_digit = '0123456789ABCDEF'

    for i in range(n):  # 10진수로 바꾼 16진수 리스트 만들기
        hex_list[i] = hex_digit.index(hex_list[i])

    bin_s = ''
    for d in hex_list:  # 바꿔준 10진수 하나씩 뽑아서 담기
        bin_s += dec_to_bin(d)

    # print(bin_s)
    m = len(bin_s)
    # print(m)
    # print(bin_s[::-1].index('1'))
    end_idx = m - bin_s[::-1].index('1')-1
    # print(end_idx)

    code = []
    code_dict = {'001101': 0,'010011':1,'111011':2,'110001':3,'100011':4,'110111':5,'001011':6,'111101':7,'011001':8,'101111':9}

    while end_idx > 6:
        code.append(code_dict[bin_s[end_idx-5:end_idx+1]])
        end_idx -= 6

    # print(code[::-1])


    print(f'#{tc} {" ".join(map(str,code[::-1]))}')