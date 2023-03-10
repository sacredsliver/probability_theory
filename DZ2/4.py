# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# а) Какова вероятность того, что все мячи белые? 
# б) Какова вероятность того, что ровно два мяча белые? 
# в) Какова вероятность того, что хотя бы один мяч белый?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# все комбинации для каждой корзины
n1=combinations(10,2)
n2=combinations(11,2)

print(f'Общее число элементарных исходов для первой корзины: n1 = {n1}\n'
f'Общее число элементарных исходов для второй корзины: n2 = {n2}')


# a) Для выполнения этого условия необходимо одновременное наступление двух событий:
# событие А-из первой корзины извлекли 2 белых шара из 7,
# событие В-из второй корзины извлекли 2 белых шара из 9.
m1=combinations(7,2)
m2=combinations(9,2)
print(f'Число благоприятных элементарных исходов для события A: m1 = {combinations(7,2)}\n'
      f'Число благоприятных элементарных исходов для события B: m2 = {combinations(9,2)}'
     )

# Для событий А и В вероятности их наступления будут расчитываться как P(A)=m1/n1 и P(B)=m2/n2 
# а вероятность их одновременного наступления как P(A+B)=P(A)*P(B)
print(f'Вероятность наступления события A, P(A) = {m1/n1: .4f}\n'
      f'Вероятность наступления события B, P(B) = {m2/n2: .4f}\n'
      f'Вероятность одновременного наступления событий A и B (что все извлечённые мячи белые), P(A+B) = {(m1/n1)*(m2/n2):.4f}'
     )


# б) Этому варианту соответствует 3 комбинации:
#   a) 2 белых + 0 белых
#   b) 0 белых + 2 белых
#   c) 1 белый + 1 белый

a1 = combinations(7, 2)
a2 = combinations(2, 2)
p1=a1/n1
p2=a2/n2
pa=p1*p2
print(f'2 белых + 0 белых pa= {pa:.4f}')


a1 = combinations(2, 2)
a2 = combinations(9, 2)
p1=a1/n1
p2=a2/n2
pb=p1*p2
print(f'0 белых + 2 белых pb= {pb:.4f}')

a1 = combinations(7, 1)
a2 = combinations(9, 1)
b1 = combinations(3, 1)
b2 = combinations(2, 1)
p1=(a1*b1)/n1
p2=(a2*b2)/n2
pc=p1*p2
print(f'1 белый + 1 белый pc= {pc:.4f}')

p=pa+pb+pc
print(f'Вероятность того, что будут вытащены ровно 2 белых мяча P = {p:.4f}')


# в) от обратного - найдём вероятность что ни один из мячей не белый
m1=combinations(3,2)
m2=combinations(2,2)

print(f'Число благоприятных элементарных исходов для первой корзины: m1 = {combinations(3,2)}\n'
      f'Число благоприятных элементарных исходов для второй корзины: m2 = {combinations(2,2)}'
     )

print(f'Вероятность того, что не будет извлечено ни одного белого мяча Р(А_обр) = {(m1/n1)*(m2/n2): .4f}\n'
      f'Вероятность того, что будет извлечен хотя бы один белый мяч Р(А) = 1 - Р(А_обр) = {1-(m1/n1)*(m2/n2): .4f}'
     )