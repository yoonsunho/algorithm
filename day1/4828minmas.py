T = int(input()) # 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0] # 첫 원소를 최댓값으로 가정
    min_v = arr[0] # 첫 원소를 최솟값으로 가정
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]


    print(f'#{tc} {max_v-min_v}')