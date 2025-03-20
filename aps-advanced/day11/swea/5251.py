import sys
sys.stdin = open("txt/5251.txt", "r")

T = int(input())
for tc in range(1, T+1):

    N, E = map(int,input().split())     # 연결지점 0~N, 간선의 개수 E(1<=N,)

    print(f'#{tc}')