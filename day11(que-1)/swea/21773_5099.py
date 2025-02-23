import sys
sys.stdin = open("txt/5099.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())        # 화덕의 크기 N, 피자의 개수 M(3<=N<=20, N<=M<=100)

    cheese = list(map(int, input().split()))







    print(f'{test_case}')