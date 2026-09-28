#ЗАКЛЮЧНИЙ ПРОЕКТ

import numpy as np
#Генерація та структура даних
gen_int = np.random.default_rng(seed=500)
sales_raw = gen_int.integers(10, 150, size=112) #Згенеровано масив на 112 випадкових чисел у діапазоні від 10 до 150
sales_matrix = sales_raw.reshape(28, 4) #Перетворюємо на матрицю 28x4

#Створення булевої маски та фільтрація
sales_matrix_booleanmask = sales_matrix > 120
peak_sales = sales_matrix[sales_matrix_booleanmask] #peak_sales буде містити пік продажів
print(f"Кількість пікових продажів: {len(peak_sales)}")

#Надійшли дані за додатковий 29-й день для всіх 4 товарів.
day_29_1 = gen_int.integers(10, 150, size=4) #Генерація масиву з рандомних 4 чисел в діапазоні від 10 до 150 
day_29 = day_29_1.reshape(1, 4)
full_sales_matrix = np.vstack((sales_matrix, day_29))

#Аналітика та Статистика
total_revenue = np.sum(full_sales_matrix) #Загальні показники суми, середнього значення, медіани по матриці
mean_revenue = np.mean(full_sales_matrix)
median_revenue = np.median(full_sales_matrix)
product_totals = np.sum(full_sales_matrix, axis=0) #Обчислити загальну суму товару за день
daily_means = np.mean(full_sales_matrix, axis=1) #Обчислити середнє арифметичне за кожний день даного товару

#У наступному місяці очікується зростання продажів на 10%.
projected_sales = full_sales_matrix * 1.10

#Форматований вивід у консоль
print("Розмірність матриці:", full_sales_matrix.shape)
print("Загальна сума та медіана нашої матриці:", total_revenue, median_revenue)
print(f"Середнє арифметичне нашої матриці: {round(mean_revenue, 2)}")
print("Загальна сума товару за день та середнє арифметичне за кожен день даного товару:", product_totals, daily_means)
print("Виведи перші 5 рядків прогнозованої матриці(зростання продажів):", projected_sales[:5]) #:5 усі перші 5 рядків
