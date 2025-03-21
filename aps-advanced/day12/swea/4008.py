import sys
sys.stdin = open("txt/4008.txt", "r")

op = ['+', '-', '*', '/']

T = int(input())
for tc in range(1, T+1):

    N = int(input())    # 숫자의 개수( 3 ≤ N ≤ 12)
    oper = list(map(int, input().split()))
    print(oper)
    op_li= []
    for i in range(4):
        op_li.extend(op[i]*oper[i])

    print(op_li)
    num_list = map(int, input().split())

    print(f'#{tc}')