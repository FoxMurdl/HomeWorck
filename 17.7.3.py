per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
deposit = []
deposit.append(per_cent['ТКБ'] * money/500)
deposit.append(per_cent['СКБ'] * money/500)
deposit.append(per_cent['ВТБ'] * money/500)
deposit.append(per_cent['СБЕР'] * money/500)
print(deposit)
print('Максимальная сумма, которую вы можете заработать:', max(deposit))