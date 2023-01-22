# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали 
# б). только две детали 
# в). хотя бы одна деталь 
# г). от одной до двух деталей?

# а) для того, чтобы произошло событие "вышли из строя все детали"
P3=0.1*0.2*0.25
print(f'Вероятность того, что из строя выйдут все детали Р(3) = {P3:.4f}')


# б) для того, чтобы произошло событие "вышли из строя 2 детали"
P2=0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(f'Вероятность того, что из строя выйдут только 2 детали Р(2) = {P2:.4f}')


# в) событие "выйдет из строя хотя бы одна деталь" можно рассмотреть как противоположное событию "не вышло из строя ни одной детали"
P0=0.9*0.8*0.75
print(f'Вероятность того, что из строя не выйдет ни одной детали Р(0) = {P0:.4f}')
P_0=1-P0
print(f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(>=1) = {P_0:.4f}')


# г) событие "из строя выйдут от 1 до 2 деталей" произойдет при наступлении события "из строя выйдет 1 деталь" или "из строя выйдут 2 детали", 
# следовательно его вероятность будет равна сумме вероятностей этих событий
P1=0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8
print(f'Вероятность того, что выйдет из строя выйдут от 1 до 2 деталей Р(1,2) = {P1+P2:.4f}')