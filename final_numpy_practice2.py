
coefficients = np.array([1.99, 0.50, 3.75, 12.10]) #Робота з дробовими показниками та відкидання дробової частини
scores = coefficients.astype(int)
print("Початковий масив float:", coefficients)
print("Масив після відкидання дробової частини:", scores)


#Дослідження матриці та явне задання типів
status_matrix = np.array([
    [True, False, True],
      [False, True, True]
], dtype= int)
print('Кількість вимірів:', status_matrix.ndim)
print('Кількість елементів:', status_matrix.shape)
print('Тип даних у матриці:', status_matrix.dtype)
total1 = status_matrix.sum()
print("Загальна сума усіх елементів у матриці:", total1)

#Підсумковий проєкт №2: «Модуль конверсії та підрахунку даних серверу»
#імпорт бібліотеки
import numpy as np
#Обробка часу відповіді (Рядки ➔ Цілі числа)
response_times_raw = np.array(["120", "85", "300", "45", "150"])
print("Початковий тип даних(string):", response_times_raw)

response_times = response_times_raw.astype(int)
print('Масив після відкидання лапок:', response_times)

#поразувати загальну суму часу:
total = response_times.sum()
print("Загальний час:", total)


#Нормалізація коефіцієнтів навантаження (Float ➔ Int)
load_factors = np.array([1.85, 0.92, 4.15, 2.70])
load_levels = load_factors.astype(int)
print("Початковий тип даних: (float):", load_factors)
print("Тип даних після відкидання дробової частини:", load_levels)

#Матриця активності серверних вузлів (2D Matrix + Explicit dtype)
nodes_status = np.array([
     [True, False],
     [True, True],
     [False, True]
], dtype=int)
print("Матриця:", nodes_status)
print("Кількість вимірів у матриці:", nodes_status.ndim)
print('Кількість елемнтів у  матриці:', nodes_status.shape)
print("Тип даних у матриці:", nodes_status.dtype)
#Обчислення загальної кількості вузлів активності
total1 = nodes_status.sum()
print("Загальна кількість вузлів активності:", total1)

