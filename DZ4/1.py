
def mean_and_variance(a,b):
    return f'На промежутке ({a};{b}]\nСреднее значение: М(А) = {(a+b)/2: .2f}\nДисперсия: D(A) = {((b-a)**2)/12: .2f}'
print(mean_and_variance(200,800))