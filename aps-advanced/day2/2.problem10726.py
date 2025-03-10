import sys
sys.stdin = open("10726.txt","r")

# M의 우측 N개를 확인할 예정
# 정석 방법
def solution():
    target = M
    for _ in range(N):      # N번 확인한다
        # 1은 0x1, 0b1, 1로 모두 사용가능
        # - 비트 연산임을 명시하기 위해 사용
        if target & 0x1 == 0:     # 맨 우측 비트가 1인지 확인
            return "OFF"        # 하나라도 0 이면 끝
        target = target >> 1    # 1 이 있으면 맨 우측 비트 삭제..
    return "ON"

# 단순하게 하는 방법
# def solution():
#     # N개의 1을 구함 (ex. 10000 - 1 = 1111)
#     mask = (1 << N) - 1
#     result = (M & mask) == mask     # 같으면
#     return result      # True or False

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    ans = solution()


    print(f'#{tc} {ans}')
