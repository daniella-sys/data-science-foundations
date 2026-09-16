import numpy as np
revenue_usd = np.array([100.0, 250.0, 400.0]) #створили вектор 1х3

#Перетворення рядка на стовпчик
revenue_col = revenue_usd[:, np.newaxis]

#Створили ще вектор 1х5
fx_rates = np.array([41.0, 41.2, 41.1, 41.5, 41.3])

#Вбудований Broadcasting
brocas = revenue_col * fx_rates

print("Результат розмірності матриці яку отримаєм:", brocas.shape)
