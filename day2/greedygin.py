# num = 456789
num = int(input())
c = [0] * 12    # 왜 12개?
                # 원래 9칸인데 두칸을 더 만들어서 triplet 검사 시 index 에러가 발생하지 않게 하기 위함
                # c[10], c[11]은 항상 0, run 확인을 위한 여분

for i in range(6):  # 단순 반복 6회
    c[num % 10] += 1    # num%10 의 1의 자리 알아내기
    num //= 10          # num 의 1의 자리 제거

i = 0
tri = run = 0

while i < 10:   # 카드 번호 9까지
    if c[i] >= 3:   # tri확인
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1: #run 확인
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
    
if run + tri == 2:
    print('Baby Gin')
else:
    print('Loose')

