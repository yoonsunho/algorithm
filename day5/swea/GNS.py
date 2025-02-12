import sys
sys.stdin = open("txt/GNS.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    tc, N = input().split()
    num_list = list(input().split())

    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    lis = {}

    new_arr = []
    for j in range(10):
        for i in range(int(N)):
            if num_list[i] == arr[j]:
                new_arr.append(num_list[i])

    print(f'{tc} {" ".join(new_arr)}')