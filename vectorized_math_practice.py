#Експрес-перерахунок цін та податків у FINTECH
import numpy as np 

# Базові суми 4 транзакцій у USD
base_amounts = np.array([100.0, 250.0, 50.0, 400.0])

# Фіксована комісія системи для кожної з 4 транзакцій (у USD)
service_fees = np.array([2.5, 5.0, 1.5, 8.0])

#Додавання
total_usd = base_amounts + service_fees

#Множення на скаляр
total_uah = total_usd * 41.5

#Віднімання
discounts_uah = np.array([50.0, 100.0, 0.0, 200.0])
final_uah = total_uah - discounts_uah

#Ділення
installment_payment = final_uah / 2

#Вивід
print(final_uah, installment_payment)
