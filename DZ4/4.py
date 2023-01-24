# Рост взрослого населения города X имеет нормальное распределение. 
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см. 
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост: 
# а). больше 182 см 
# б). больше 190 см 
# в). от 166 см до 190 см 
# г). от 166 см до 182 см 
# д). от 158 см до 190 см 
# е). не выше 150 см или не ниже 190 см 
# ё). не выше 150 см или не ниже 198 см 
# ж). ниже 166 см.

from scipy.stats import norm

mu=174
sigma=8

# а). больше 182 см
pa=1-norm.cdf(182, mu, sigma)
print(pa)

# б). больше 190 см
pb=1-norm.cdf(190, mu, sigma)
print(pb)

# в). от 166 см до 190 см 
pv=norm.cdf(190, mu, sigma)-norm.cdf(166, mu, sigma)
print(pv)

# г). от 166 см до 182 см 
pg=norm.cdf(182, mu, sigma)-norm.cdf(166, mu, sigma)
print(pg)

# д). от 158 см до 190 см 
pd=norm.cdf(190, mu, sigma)-norm.cdf(158, mu, sigma)
print(pd)

# е). не выше 150 см или не ниже 190 см 
pe=norm.cdf(150, mu, sigma)+1-norm.cdf(190, mu, sigma)
print(pe)

# ё). не выше 150 см или не ниже 198 см 
pyo=norm.cdf(150, mu, sigma)+1-norm.cdf(198, mu, sigma)
print(pyo)

# ж). ниже 166 см.
pzh=norm.cdf(166, mu, sigma)
print(pzh)