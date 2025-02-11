s1 = 'ab'* 6
print(s1)   # abababababab
s = ['a', 'b', 'c']
print('.'.join(s))  # a.b.c

txt = list(input())     # abcde
N = len(txt)
for i in range(N//2):   # 홀, 짝 모두 동일(몫)
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]

print(txt)  # ['e', 'd', 'c', 'b', 'a']

# 연습문재 1
s = 'string'
s = s[::-1]
print(s, type(s))   # gnirts <class 'str'>
s_list = list(s)
s_list.reverse()
print(s_list)   # ['s', 't', 'r', 'i', 'n', 'g']
print(''.join(s_list))  # string

# 연습문제2 (회문)
N = 4
txt = input()
total = 0
for j in range(8 - N +1):   # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N //2):  # 회문 길이의 절반만큼 비교(바꾸기)
        if txt[j+k] != txt[j+N-1-k]:
            break   # 비교 글자라 다르면 현재 구간 중지
    else:   # break에 걸리지 않고 for 종료, 회문이면
            # txt[j], txt[j+N-1-k] = txt[j+N -1-k], txt[j+k]
            total += 1
print(total)