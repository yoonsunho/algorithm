import sys
sys.stdin = open("txt/5202.txt", "r")

# 모르겡ㅁ
T = int(input())
for tc in range(1, T+1):
    
    N = int(input())        # 신청서의 갯수

    time =[[]* N for _ in range(N)]



    for i in range(N):
        [s, e] = list(map(int, input().split()))        #  0<=s<24, 0 ＜ e ＜= 24
        time[i] = [s,e]

    print(time)

    



    print(f'#{tc}')