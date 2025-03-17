import sys
sys.stdin = open("txt/1952.txt", "r")

T = int(input())
for tc in range(1, T+1):

    cost = list(map(int, input().split()))       # 1일, 1달, 3달, 1년 이용권 가격들

    monthly_plan = list(map(int, input().split()))

    print(monthly_plan)


    print(f'#{tc}')