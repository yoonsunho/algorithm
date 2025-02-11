s1 = 'abc'
s2 = 'ab'
s3 = 'def'
s4 = s2 + 'c'
print(s1 == s4)     # True(값 비교)
print(s1, s4)       # abc abc
print(s1 is s4)     # False(메모리 주소 비교) # 내용은 같지만 서로 다른 곳을 참조함
print(s1 is 'abc')      # True
print(s4 is 'ab'+'c')   # False

print('--------------------------')

# 숫자, 대문자, 소문자 순
s1 = 'ab'
s2 = 'ab'
s3 = 'ab'
s4 = 'AC'
s5 = 'abc'
s6 = '1ab'
print(s1 == s2)     # True
print(s1 < s2)      # False
print(s1 < s3)      # False
print(s3 < s4)      # False
print(ord('a'), ord('A'))   # 97 65 #대문자 먼저
print(s1 < s5)      # True
print(s5 > s6)      # True
print(s4 < s6)      # False # 숫자(먼저) < 대문자(나중)
print('A' < '@')    # False

print('=====================')
a = 'F'
b = int(a, 16)  # 16진수로 변환
c = '1001'
d = int(c, 2)   # 2 진수로 변환
print(b)    # 15
print(d)    # 9 (1+8)

print('----------------')
s = '123'
def atoi(st):
    i = 0
    for x in st:
        i = i*10 + ord(x)-ord('0')
    return i

a= atoi(s)
print(a+1)  # 124