import numpy as np
quantities = np.array([100, 250, 500]) #Вектор 1х3
prices = np.array([50.0, 120.0, 30.0]) #Ще один вектор 1х3

base_revenue = quantities * prices

#Перетворення рядка на стовпець 
base_revenue_col = base_revenue[:, np.newaxis] 

#Broadcasting між масивами різної розмірності:
region_discounts = np.array([0.0, 0.05, 0.10, 0.15]) #Створення вектора 1х4
discounted_revenue = base_revenue_col * (1 - region_discounts) #Спрацьоє вбудований Broadcasting оскільки підлаштує розмірність 

final_revenue = discounted_revenue * 1.20

#Вивід 
print("Матрицю, яку отримали її розмірність:", final_revenue.shape)
