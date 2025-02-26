import sys
sys.stdin = open("txt/4831.txt","r")

# 25분
# 혼자 풀었는데 기발하게 잘 푼것 같음

T =int(input())
for tc in range(1, T+1):

    K,N,M = map(int, input().split())   # k: 한번 충전으로 이동할 수 있는 최대 정류장 수 N: 버스정류장 0~N번 , M: 충전기 설치된 정류장 개수

    charging = list(map(int, input().split()))

    current = 0      # 현재 위치 인댁스
    cnt = 0     # 충전횟수 담을 변수

    while current + K < N:
        for i in range(current+K, current, -1):
            if i in charging:
                cnt += 1
                current = i
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')