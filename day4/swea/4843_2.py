import sys
sys.stdin = open("txt/4843_input.txt", "r")
# 다시 풀어보기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())  # N개의 정수 10<=N<=100
    a = list(map(int, input().split()))  # 1<=ai<=100

    c = [0] * 10     # 특이한 정렬을 담을 배열

    for k in range(10):
        max_idx, max_v = 0, a[0]
        min_idx, min_v = 0, a[0]
        for i in range(N-k):
            if max_v < a[i]:
                max_idx, max_v = i, a[i]
            if min_v > a[i]:
                min_idx, min_v = i, a[i]
        if k % 2 == 0:
            c[k] = a.pop(max_idx)
        else:
            c[k] = a.pop(min_idx)

    
    print(f'#{test_case} {" ".join(map(str, c))}')