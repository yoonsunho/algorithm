import sys
sys.stdin = open("txt/21649.txt", "r")

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = int(input().split())     # 정점의 개수(V)와 간선의 개수(E)

    arr = list(map(int, input().split()))       # 연결 정점들
