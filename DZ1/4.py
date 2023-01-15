# В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
import numpy as np

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

# P(A)=m/n - общее количество исходов будет определяться количеством сочетаний n = 2 из 100,
# а количество благоприятных исходов m = 1

P=1/combinations(100,2)
print(f'P(оба выигрышных) = {round(P*100,2)}%')