'''
0<=DATA[i]<=4조건
'''
# counting 정렬 사용되려면, DATA가 INDEX값으로 표현되는 자료여야함,,
DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)
COUNTS = [0]*5  # max(DATA)+1
TEMP = [0] * N  # 정렬 결과 저자

# 1단계
for i in range(N):  # 각 숫자의 개수
    COUNTS[DATA[i]] += 1

print(COUNTS)   # [1, 3, 1, 1, 2]

# 2단계
for i in range(1, 5):    # COUNTS[i] 까지의 합계
    COUNTS[i] += COUNTS[i-1]

print(COUNTS)   # [1, 4, 5, 6, 8]

# 3단계
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1    # DATA[i]까지의 개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]     # DATA[i] 까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록

print(TEMP)

