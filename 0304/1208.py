import sys
sys.stdin = open("txt/1208.txt","r")

# 1 시간 넘게 걸리고 못품
# 다시 풀기

for tc in range(1, 11):

    N = int(input())        # 덤프 횟수
    hei = list(map(int, input().split()))   # 건물의 높이 1<=hei<= 100

    for _ in range(N):
        
        # for 문 안에 써야 함 주의
        min_idx, min_v = 0, hei[0]
        max_idx, max_v = 0, hei[0]

        # 최댓갑 최소값 구하기
        for i in range(100):
            if hei[i] > max_v:
                max_idx, max_v = i, hei[i]
            # elif 라 써도 됨
            elif hei[i] < min_v:
                min_idx, min_v = i, hei[i]

        if max_v - min_v <= 1:
            break

        hei[max_idx] -= 1
        hei[min_idx] += 1


    print(f'#{tc} {max(hei)- min(hei)}')