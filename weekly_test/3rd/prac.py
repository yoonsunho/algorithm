import math

# 두 점 사이 거리 구하기, 각도
start = (1,1)
end = (2,2)

a = abs(end[0]-start[0])
b = abs(end[1]- start[1])

r = math.sqrt(a**2 + b**2)

radian = math.atan(b/a)

print(r, math.degrees(radian))

# 쿠션 구하기

PI = 3.141592

def calculate(x1,x2,y1,y2):
    a = x2 - x1
    b = y1 + y2
    radian= math.atan(a/b)
    return radian

x1, y1 = 1.0, 2.0
x2, y2 = 5.0, 1.0

alpha = calculate(x1,y1,x2,y2)

print(f'myball의 출발 각도 (라디안):{alpha}')
print(f'myball의 춟발 각도(도):{math.degrees(alpha)}')

print(f'myball의 춟발 각도(도):{alpha*(180.0/PI)}')

# 스트레이트 샷 - 분리각 계산법
'''
다음은 공과 홀의 위치입니다. 내 공(my ball)을 목표구(target)를 거쳐 홀(Hole)로 넣기 위해 
필요한 각도(θ), 거리(d), 그리고 충돌 후 목표구의 이동 거리 및 필요한 초기 속도(v)를 구하세요.

my ball 위치: (1, 2)

target 위치: (5, 6)

Hole 위치: (9, 8)

공의 반지름(r): 1

마찰 계수(μ): 0.2
'''

my_ball = (1, 2)
target = (5, 6)
hole = (9, 8)
print(math.radians(42.33))


