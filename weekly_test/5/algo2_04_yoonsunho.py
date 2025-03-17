# 완전이진트리
def pre_order(i, bl):   # 전위 순회
    global N
    global pre_num
    if i <= N:
        pre_num += str(bl[i])
        # print(bl[i], end='')
        pre_order(2*i, bl)
        pre_order(2*i+1, bl)


def in_order(i, bl):    # 중위 순회
    global N
    global in_num
    if i <= N:
        in_order(2 * i, bl)
        in_num += str(bl[i])
        # print(bl[i], end='')
        in_order(2 * i + 1, bl)

def post_order(i, bl):  # 후위 순회
    global N
    global post_num
    if i <= N:
        post_order(2 * i, bl)
        post_order(2 * i + 1, bl)
        post_num += str(bl[i])
        # print(bl[i], end='')

def bin_to_dec(s):  # 2진수 -> 10진수
    dec_num = 0
    pow = 0     # 지수

    for x in reversed(s):
        if x == "1":
            dec_num += 2**pow
        pow += 1
    return dec_num

T = int(input())
for tc in range(1, T+1):

    N = int(input())    # 정점의 개수
    arr = list(map(int, input().split()))    # 각 정점에 들어있는 값 표기
    # print(arr)
    bin_list = [0]
    bin_list.extend(arr)
    # print(bin_list)

    pre_num, in_num, post_num = '', '', ''      # 2진수 값을 str로 담을 것임

    max_num = 0
    pre_order(1, bin_list)

    in_order(1, bin_list)
    # print()
    post_order(1, bin_list)
    # print(pre_num,in_num,post_num)
    max_num = max(bin_to_dec(pre_num), bin_to_dec(in_num), bin_to_dec(post_num))
    # print(max_num)

    # print(int('1001',2))

    print(f'#{tc} {max_num}')