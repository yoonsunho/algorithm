import sys
sys.stdin = open("txt/1215.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    str_list = [list(input()) for _ in range(8)]


    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            word = str_list[i][j:j+N]
            for k in range(N//2):
                if word[k] != word[N-1-k]:
                    break
            else:
                cnt += 1

    reverse_str = list(map(list, zip(*str_list)))
    for i in range(8):
        for j in range(8 - N + 1):
            word = reverse_str[i][j:j+N]
            for k in range(N//2):
                if word[k] != word[N-1-k]:
                    break
            else:
                cnt += 1

    print(f'#{test_case} {cnt}')