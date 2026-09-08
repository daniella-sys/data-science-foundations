#Аналіз погодинних продажів інтернет-магазину
import numpy as np
hourly_orders = np.arange(24)
print("Розмірність нашого масиву:", hourly_orders.shape)

# Перетворення на добову сітку (4 x 6)
sales_4x6 = hourly_orders.reshape(4, 6)
print("Розмірність нашого масиву:", sales_4x6)

#Автоматичний розрахунок за допомогою -1
sales_half_day = hourly_orders.reshape(2, -1) #за формулою це буде 24/2=12 стовпців
print("Розмірність нашого масиву:", sales_half_day.shape)

#Сплющення даних назад у 1D-вектор та перевірка копії
flat_sales = sales_4x6.flatten() #сплющили матрицю 4х6 на послідовний рядок(вектор)
flat_sales[1] = 5678
print("Сплющена матриця 4х6:", flat_sales)
print("Матриця до сплющення:", sales_4x6)



