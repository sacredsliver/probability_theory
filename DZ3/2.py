# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

from math import factorial

def combinations(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

P1=(combinations(3,2)/combinations(8,2))*(combinations(5,3)*combinations(7,1)/combinations(12,4))
print(f'Вероятность события "из первой корзины не вытащили ни одного белого мяча'
      f', из второй вытащили 3 белых мяча"\nP(A1) = {P1:.4f}'
     )

P2=(combinations(5,1)*combinations(3,1)*combinations(5,2)*combinations(7,2))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 1 белый мяч'
      f', из второй вытащили 2 белых мяча"\nP(A2) = {P2:.4f}'
     )

P3=(combinations(5,2)*combinations(5,1)*combinations(7,3))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 2 белых мяча'
      f', из второй вытащили 1 белый мяч"\nP(A2) = {P3:.4f}'
     )

print(f'Вероятность того, 3 мяча белые Р(А) = {P1+P2+P3:.4f}')