# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
from math import factorial

def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))

# Так как кнопки нажимаются одновременно, то порядок не важен, и для формулы вероятности P(A)=m/n
# общее число исходов будет определяться количиством сочетаний n = 3 из 10, 
# а количество благоприятных исходов m=1 замок открылся

P=1/combinations(10,3)
print(f'P(открыть с первой попытки) = {round(P*100,2)}%')