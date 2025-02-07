# loop를 이용하여 부분집합 생성하기
bit = [0] * 4
for i in range(2):
    bit[0]= i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
    print(bit)



#
a= [2,3,7]
bit = [0] * 3
for i in range(2):
    bit[0]= i
    for j in range(2):
        bit[1]= j
        for k in range(2):
            bit[2]= k
            # print(bit)
            s=0             # 부분 집합의 합
            for b in range(3):
                if bit[b]:
                    print(a[b], end=' ')    # 부분집합에 포함된 원소
                    s += a[b]
            print(bit,s)