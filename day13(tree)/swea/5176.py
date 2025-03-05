import sys
sys.stdin = open("txt/5176.txt", "r")

T = int(input())
for tc in range(1, T+1):

    N = int(input())      # 정점의 수
    E = N - 1            # 간선의 수



    print(f'#{tc}')