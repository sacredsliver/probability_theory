# О случайной непрерывной равномерно распределенной величине B известно, что ее
# дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая
# граница равна 0.5?
# Если да, найдите ее.

b=0.5+2.4**(1/2)
print(f'Левая граница распределения величины В - b = {b: .3f}\n'
      f'Среднее значение В на промежутке (0.5; {b: .3f}) M(B) = {(b+0.5)/2: .3f}'     
     )