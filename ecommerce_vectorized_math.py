#Експрес-перерахунок цін та податків у FINTECH
import numpy as np 

# Собівартість (оптова ціна) 4 товарів у грн
cost_price = np.array([500.0, 1200.0, 300.0, 2500.0])

# Торгова націнка магазину на кожен товар (у грн)
markup = np.array([150.0, 400.0, 100.0, 800.0])

#Додавання
retail_price = cost_price + markup

#Віднімання
discounts = np.array([50.0, 100.0, 30.0, 200.0]) 
discounted_price = retail_price - discounts

#Множення
sales_volume = np.array([3, 3, 3, 3])
total_revenue = discounted_price * sales_volume

#Ділення
margin_pct = (discounted_price - cost_price) / discounted_price * 100

#Піднесення до квадрата 
factors = np.array([1.05, 1.10, 1.02, 1.15])
decay_factors = factors ** 2 

#Вивід
print(total_revenue, margin_pct, decay_factors)
