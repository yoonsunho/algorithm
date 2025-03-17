import sys
sys.stdin = open("txt/4366.txt")

def bin_test(num):

    for i in range(len(num)):
        new_num = num[:]
        # print(new_num)
        new_num[i] = 1 - num[i]
        bin_list.append(new_num)
        # print(bin_list)

def thr_test(num):

    for i in range(len(num)):
        if num[i] == 0:
            for a in [1, 2]:
                new_num = num[:]
                new_num[i] = a
                # print(new_num)
                thr_list.append(new_num)
        elif num[i] == 1:
            for a in [0, 2]:
                new_num = num[:]
                new_num[i] = a
                thr_list.append(new_num)
        elif num[i] == 2:
            for a in [0, 1]:
                new_num = num[:]
                new_num[i] = a
                # print(new_num)
                thr_list.append(new_num)
                # print(thr_list)

def bin_to_dec(n):
    dec_num = 0
    pow = 0

    for x in n[::-1]:
        if x == 1:
            dec_num += 2 ** pow
        pow += 1

    return dec_num

def thr_to_dec(n):
    dec_num = 0
    pow = 0

    for x in n[::-1]:
        if x == 1 or x == 2:
            dec_num += x*(3**pow)
        pow += 1

    return dec_num

T = int(input())
for tc in range(1, T+1):

    bin = list(map(int,input()))
    thr = list(map(int,input()))

    bin_list = []   # 하나씩 수정한 이진수 담을 리스트
    thr_list = []   # 하나씩 수정한 3진수 담을 리스트

    bin_test(bin)
    thr_test(thr)
    # print(bin_list)
    # print(thr_list)
    # print(len(thr_list))

    bin_l = [0]*len(bin_list)
    thr_l = [0]*len(thr_list)

    for i in range(len(bin_list)):
        bin_l[i] = bin_to_dec(bin_list[i])

    for i in range(len(thr_list)):
        thr_l[i] = thr_to_dec(thr_list[i])

    # print(bin_l)
    # print(thr_l)

    ans = 0
    for x in bin_l:
        if x in thr_l:
            ans = x



    print(f'#{tc} {ans}')