# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

# воспользуемся формулой Бернулли 
# n=144, k=70, p=0.5
def bernulli(n, k, p):
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)

print(f'Вероятность что орёл выпадет ровно 70 раз: P = {bernulli(144,70,0.5):.4f}')