import sys
sys.stdin = open("txt/5250.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def prim(st):



T = int(input())
for tc in range(1, T+1):

    N = int(input())    # 가로 세로 칸 수 3<=N<=100
    hei = [list(map(int, input().split())) for _ in range(N)]

    prim([0,0])


    print(f'#{tc}')