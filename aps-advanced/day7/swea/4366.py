import sys
sys.stdin = open("txt/4366.txt", "r")

def bin_test(num):

    for i in range(len(num)):
        new_num = num[:]
        # print(new_num)
        new_num[i] = 1 - num[i]
        bin_list.append(new_num)
        # print(bin_list)

def thr_test(num):

    for i in range(len(num)):
        new_num = num[:]
        if num[i] == 0:
            for a in [1, 2]:
                new_num[i] = a
                # print(new_num)
                thr_list.append(new_num)
        elif num[i] == 1:
            for a in [0, 2]:
                new_num[i] = a
                thr_list.append(new_num)
        elif num[i] == 2:
            for a in [1, 0]:
                new_num[i] = a
                thr_list.append(new_num)



T = int(input())
for tc in range(1, T+1):

    bin = list(map(int,input()))
    thr = list(map(int,input()))

    bin_list = []
    thr_list = []

    bin_test(bin)
    thr_test(thr)
    print(bin_list)
    print(thr_list)

    for i in range(len(bin_list)):
        for j in range(len(bin_list[0])):




    print(f'#{tc}')