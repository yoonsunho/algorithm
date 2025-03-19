import sys
sys.stdin = open("txt/5648.txt", "r")

di= [-1,1,0,0]
dj = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):

    N = int(input())    # 원자의 수

    idx_i, idx_j = [0] * (N), [0]*N
    for i in range(N):


    print(f'#{tc}')