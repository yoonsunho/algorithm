# 회문2
# 강사님 풀이
# 가장 긴 길이의 회문부터
# 길이 100번일 때 1번 비교
# 99일땐 2번 
# 98 일 땐 3번

import sys
sys.stdin = open('txt/1216.txt')

# 회문확인 함수
# 처음과 끝이 다르면 바로 return False로 인해서 속도가 훨씬 빠르다
def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# 회문확인 조금 더 느린 버전
def is_palindrome_simple(string):
    return string == string[::-1]

def find_longest_palindrome(matrix):
    max_length = 1  # 가장 긴 회문의 글자 수를 저장할 변수

    # 긴 길이부터 검사(100, 99, 98,...2)
    for length in range(N, 1, -1):  # 길이가 100인 회문이 있는지 먼저 검사, 다음은 99
        # 행을 하나 잡고, 그 행에 있는 회문을 찾자
        for i in range(N):  # i= 0 => 1행 잡아두고
            for start in range(N-length + 1):    # 해당 행에서 주어진 회문의 길이를 몇번 실행하는지
                # 행 검사
                if is_palindrome(matrix[i][start: start + length]):
                    # 회문을 찾았으면 바로 길이 반환( 왜냐면 가장 긴것부터 찾았으니까)
                    return length

                # 열 검사
                column = []
                # i 열을 고정해 놓고, [start, start+legth] 잘라서 열별로 접근해서 하나의 리스트애 담는다.
                for j in range(start, start+length):
                    column.append(matrix[j][i])

                # 열을 담은 리스트를 대상으로 회문검사한다.
                if is_palindrome(column):
                    return length

    return max_length

for test_case in range(1,11):
    tc = int(input())
    N = 100
    matrix = [input() for _ in range(N)]

    result = find_longest_palindrome(matrix)
    print(f'#{tc} {result}')