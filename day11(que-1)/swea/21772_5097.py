import sys
sys.stdin = open("txt/5097.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # N개의 숫자, M번의 반복
    N, M = map(int,input().split())     # 3<=N<=100, N<=M<=1000

    arr = list(map(int, input().split()))
    new_arr = [0] * N

    for _ in range(M):
        for i in range(N):
            new_arr[i] = arr[(N+i+1) % N]
        # arr = new_arr # 이렇게 쓰면 안됨, 이렇게 쓰면 같은 메모리 주소 참조하게됨
        arr = new_arr[:]    # 이런식으로 깊은 복사를 해줘야 i반복이 끝날때만 실행하게 만들 수 있음




    print(f'#{test_case} {new_arr[0]}')