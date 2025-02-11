print(f'{ord("대"):x}')  # b300
# 0x : 16진수 처리
print(chr(0xb300))  # 대

# abc입력시
s1 = list(input())
print(s1)   # ['a', 'b', 'c']
s2 = input()
print(s2)   # abc
print(s1[1])    # b
print(s2[1])    # b
s1[1]='e'
print(s1)   # ['a', 'e', 'c']
# s2[1] = '3'   # str' object does not support item assignment
s2 = 'aec'
print(s2)   # aec :가능