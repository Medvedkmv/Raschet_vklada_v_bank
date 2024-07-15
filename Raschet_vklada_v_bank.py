per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму денег, которую человек планирует положить под проценты:"))
percent_values = list(per_cent.values())
deposit = [i * money / 100 for i in percent_values]
print ("Накопленные средства за год вклада в каждом из банков:", deposit)
print("Максимальная сумма, которую можно заработать:", max(deposit))