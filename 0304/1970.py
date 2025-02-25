import sys
sys.stdin = open("txt/1970.txt", "r")

def cash(n):
    if n >= 50000:
        arr[0] = n // 50000
        cash(n % 50000)
    elif n >= 10000:
        arr[1] = n // 10000
        cash(n % 10000)
    elif n >= 5000:
        arr[2] = n // 5000
        cash(n % 5000)
    elif n >= 1000:
        arr[3] = n // 1000
        cash(n % 1000)
    elif n >= 500:
        arr[4] = n//500
        cash(n % 500)
    elif n >= 100:
        arr[5] = n // 100
        cash(n % 100)
    elif n >= 50:
        arr[6] = n // 50
        cash(n % 50)
    elif n >= 10:
        arr[7] = n // 10



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())        # 10 ≤ N ≤ 1,000,000

    arr = [0] * 8
    cash(N)
    # print(arr)



    print(f'#{test_case}')
    print(" ".join(map(str,arr)))