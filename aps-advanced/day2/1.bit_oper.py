print(7 & 5)  # 5
print(7 or 5)  # 7
print(bin(7 & 5))  # 0b101

# 1. 이진수로 변환
# 2. 각 자리를 and, or연산한다

# 1 * 3
# 16 * 10
# 16^2 * 4
print(0x4A3)  # 1187
print(bin(0x4A3 | 25))  # 0b10010111011

secret_code = 1004
print(7070 ^ secret_code)  # 6258
print(6258 ^ secret_code)  # 7070

# ----------------shift 연산자
# ----------- shift 연산자
print(1 << 1, bin(1 << 1))  # 2
print(1 << 2, bin(1 << 2))  # 4
print(1 << 3, bin(1 << 3))  # 8
print(1 << 4, bin(1 << 4))  # 16

print(7 >> 1)  # 3( 오른으로 갈 데 없으면 비트 삭제)

num = 1
for _ in range(5):
    print(num, bin(num))
    num = num << 1  # 왼 갈데 없으면 뒤에 0 추가

# ----------------- bit 연산의 응용
# 1. 부분집합의 수를 바로 구할 수 있다
arr = [1, 2, 3, 4]  # 16개

print(f'부분 집합의 수: {1 << len(arr)}')

for i in range(1 << len(arr)):  # 부분집합의 수 만큼 반복
    for idx in range(len(arr)):
        # (1 << idx): ob1, ob10, ob100, ob1000
        # i 의 idx번째 bit가 1 인지 확인( 부분 집합에 포함되어 있는지 확인)
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()

# 응용. 합이 10 인 부분집합 출력해라
for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'합이 10인 부분집합: {subset}')  # 합이 10인 부분집합: [1, 2, 3, 4]

# ----------------- 음수 표현
print(bin(5))  # 0b101
print(bin(-5))  # -0b101

